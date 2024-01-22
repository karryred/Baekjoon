"""
�� �������� �ð��ʰ��� ���� �������� �߿��� �κ��� 2���� �ֽ��ϴ�.

1. ü���� ���� Ž��
���ոα� BFS�� ��� ĭ�� ���Ͽ� �����ϸ� ������ ���� �ð��� �ɸ� ���Դϴ�. 
�̸� �湮 ó���� ���Ͽ� �̹� ���� ���� ���� �� �̻� Ž������ �ʰ� ������ �־ ����� �ð��� �ɸ��ϴ�.
�̶�, �ð��� ���̱� ���Ͽ� �ǳʶٸ� Ž���� ������ �� �ֽ��ϴ�. 
���� 4x4��� (0,0) (0,2) (1,1) (1,3) ...... �̷� ������ Ž���� �����մϴ�.
�̷��� Ž������ �� "�� ĭ���� �ǳʶپ ������ ������ ����?"��� �ǹ��� �� �� �ֽ��ϴ�.
(0,1) ĭ���� ������ �����Ϸ��� ���� ĭ�� (0,0) (0,2) (1,1)�� �ֽ��ϴ�. ���⼭ ��� �� (0,1) ���� (0,2)�� ������ �δ� �Ͱ� (0,2) ���� (0,1)�� ������ �δ� �� ���� �����Դϴ�.
ü���� Ž���� ������ ��, (0,2)�� �ǳʶٴ� ��� (0,2)�� ���ոαⰡ ������ (0,0) (0,2) (1,1)�� ���� Ž�����ִ� (0,2)���� ���� �α⸦ �����ϴ� ����� �� �������� �������شٰ� �����ϸ� ������ ���Դϴ�.

2. ���� ���ɼ�
�� �������� �� �� ���� �ξ��� �������� ���� ���� ���� �α��� �����մϴ�.
�̴� �� ������ ���̿����� �α������� �Ͼ �� ���ٴ� ���� �ǹ��մϴ�.
���� �� day�� � ���տ��� �α� ������ �Ͼ�ٸ�, �ش� ���ճ����� �α� ������ �Ұ����ϸ� ������ �α� ���� ���ɼ��� �α� ������ �Ͼ ���հ� �� ���� ������ ������ �ξ� �߻��ϴ� �α� �����Դϴ�.
���� ���� day�� Ž���� �α� ������ �Ͼ ������ �����ؼ� Ž�����ָ� �˴ϴ�.
"""

import sys
from collections import deque

input=sys.stdin.readline
N,L,R=map(int,input().split())
country=[]
move=((0,-1),(0,1),(-1,0),(1,0)) #left right top bottom
day=0
Q=deque()
possible=deque([(y, x) for y in range(N) for x in range(y % 2, N, 2)]) #ü���� ���� Ž��
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
            
            if ny<0 or ny>=N or nx<0 or nx>=N or visited[ny][nx]==day: #�̹� ���� �湮�� ��� ��ŵ
                continue
            if L<=abs(country[y][x]-country[ny][nx]) and abs(country[y][x]-country[ny][nx])<=R:
                Q.append((ny,nx))
                union.append((ny,nx))
                visited[ny][nx]=day
                
    return union    


while possible: #�α� ���� ���ɼ��� �ִ� ������
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