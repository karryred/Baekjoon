from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[[1]*(M+2)]
virus_arr=[[1]*(M+2)]
move=((-1,0),(1,0),(0,-1),(0,1))
for _ in range(N): #인덱스 범위 체크의 효율성을 위해 배열 바깥에 1을 벽으로 둘러주었습니다
    temp=[1]+list(map(int,input().split()))+[1]  
    arr.append(temp)
    virus_arr.append(temp)
arr.append([1]*(M+2))
virus_arr.append([1]*(M+2))
maximum=0
            
def checkSafe():
    global maximum

    cnt=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if not virus_arr[i][j]: 
                cnt+=1
            elif virus_arr[i][j]==3: #해당 자리의 요소가 3일 경우 0으로 다음 계산을 위해 회수해줍니다
                virus_arr[i][j]=0

    if maximum<cnt:
        maximum=cnt

"""
벽이 세워져있는 원본 배열은 그대로 두고 virus_arr에다가 BFS를 이용하여 바이러스를 전염시킵니다
만약 원본 배열을 Deep Copy 하는 방식으로 코드를 작성한다면, Depp copy의 과정에서 소모되는 자원이 많기 때문에 비효율적입니다
따라서 virus_arr배열에 바이러스를 전염시키고 회수하는 방식으로 코드를 작성하였습니다
"""
def BFS(arr):
    Q=deque()
  
    for i in range(1,N+1):
        for j in range(1,M+1):
            if arr[i][j]==2:
                Q.append((i,j))
                
    while Q:
        y,x=Q.popleft()
        
        for dy,dx in move:
            ny=y+dy
            nx=x+dx
            if not virus_arr[ny][nx]: #배열 바깥에 벽을 두르지 않았다면 4개의 대소비교 조건이 필요해집니다
                virus_arr[ny][nx]=3 
                Q.append((ny,nx)) 

    checkSafe()

def makeWall(cnt):
    if cnt==3:
        BFS(arr)
        return 

    else:
        for i in range(1,N+1):
            for j in range(1,M+1):
                if arr[i][j]==0:
                    arr[i][j]=1
                    virus_arr[i][j]=1 #벽을 virus_arr 배열에도 같이 세워줍니다
                    makeWall(cnt+1)
                    arr[i][j]=0 #벽을 회수해줍니다
                    virus_arr[i][j]=0

def debugging(array):
    for i in range(1,N+1):
        for j in range(1,M+1):
            print(array[i][j],end=" ")
        print()
    print()

makeWall(0)
print(maximum)