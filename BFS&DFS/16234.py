"""
이 문제에서 시간초과를 겪지 않으려면 중요한 부분이 2가지 있습니다.

1. 체스판 형태 탐색
연합맺기 BFS를 모든 칸에 대하여 실행하면 굉장히 오랜 시간이 걸릴 것입니다. 
이를 방문 처리를 통하여 이미 연합 맺은 곳은 더 이상 탐색하지 않게 제한을 주어도 상당한 시간이 걸립니다.
이때, 시간을 줄이기 위하여 건너뛰며 탐색을 진행할 수 있습니다. 
만약 4x4라면 (0,0) (0,2) (1,1) (1,3) ...... 이런 식으로 탐색을 진행합니다.
이렇게 탐색했을 때 "저 칸들을 건너뛰어도 무방한 이유가 뭐냐?"라는 의문이 들 수 있습니다.
(0,1) 칸에서 연합을 시작하려면 다음 칸은 (0,0) (0,2) (1,1)이 있습니다. 여기서 사실 상 (0,1) 에서 (0,2)로 연합을 맺는 것과 (0,2) 에서 (0,1)로 연합을 맺는 건 같은 연합입니다.
체스판 탐색을 진행할 때, (0,2)를 건너뛰는 대신 (0,2)와 연합맺기가 가능한 (0,0) (0,2) (1,1)을 전부 탐색해주니 (0,2)에서 연합 맺기를 시작하는 결과를 세 지점에서 포함해준다고 생각하면 수월할 것입니다.

2. 변동 가능성
이 문제에서 한 번 연합 맺어진 국가들은 전부 같은 수의 인구를 유지합니다.
이는 그 국가들 사이에서는 인구변동이 일어날 수 없다는 것을 의미합니다.
만약 전 day에 어떤 연합에서 인구 변동이 일어났다면, 해당 연합끼리는 인구 변동이 불가능하며 유일한 인구 변동 가능성은 인구 변동이 일어난 연합과 그 외의 국가가 연합을 맺어 발생하는 인구 변동입니다.
따라서 다음 day의 탐색은 인구 변동이 일어난 국가에 한정해서 탐색해주면 됩니다.
"""

import sys
from collections import deque

input=sys.stdin.readline
N,L,R=map(int,input().split())
country=[]
move=((0,-1),(0,1),(-1,0),(1,0)) #left right top bottom
day=0
Q=deque()
possible=deque([(y, x) for y in range(N) for x in range(y % 2, N, 2)]) #체스판 형태 탐색
visited = [[-1]*N for _ in range(N)]

for _ in range(N):
    country.append(list(map(int,input().split())))

def BFS(y,x):
    visited[y][x]=day
    union=[]
    Q.append((y,x))
    union.append((y,x))
    
    while Q:
        y,x=Q.popleft()
        
        for dy,dx in move:
            ny=y+dy
            nx=x+dx
            
            if ny<0 or ny>=N or nx<0 or nx>=N or visited[ny][nx]==day: #이미 오늘 방문한 경우 스킵
                continue
            if L<=abs(country[y][x]-country[ny][nx]) and abs(country[y][x]-country[ny][nx])<=R:
                Q.append((ny,nx))
                union.append((ny,nx))
                visited[ny][nx]=day
                
    return union    


while possible: #인구 변동 가능성이 있는 국가들
    for _ in range(len(possible)):
        y,x = possible.popleft()
        if visited[y][x]<day:
            union = BFS(y,x)

            if len(union)>1:
                population = 0
                for i,j in union:
                    population+=country[i][j]
                population=population//len(union)
                for i,j in union:
                    country[i][j]=population
                    possible.append((i,j))

    day+=1

print(day-1)
                  
def debugging():
    print("-----country array-----")
    for i in range(N):
        for j in range(N):
            print(country[i][j], end=" ")
        print()
    print("-----visitied array-----")
    for i in range(N):
        for j in range(N):
            print(visited[i][j], end=" ")
        print()