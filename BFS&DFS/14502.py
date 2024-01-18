from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[[1]*(M+2)]
virus_arr=[[1]*(M+2)]
move=((-1,0),(1,0),(0,-1),(0,1))
for _ in range(N): #�ε��� ���� üũ�� ȿ������ ���� �迭 �ٱ��� 1�� ������ �ѷ��־����ϴ�
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
            elif virus_arr[i][j]==3: #�ش� �ڸ��� ��Ұ� 3�� ��� 0���� ���� ����� ���� ȸ�����ݴϴ�
                virus_arr[i][j]=0

    if maximum<cnt:
        maximum=cnt

"""
���� �������ִ� ���� �迭�� �״�� �ΰ� virus_arr���ٰ� BFS�� �̿��Ͽ� ���̷����� ������ŵ�ϴ�
���� ���� �迭�� Deep Copy �ϴ� ������� �ڵ带 �ۼ��Ѵٸ�, Depp copy�� �������� �Ҹ�Ǵ� �ڿ��� ���� ������ ��ȿ�����Դϴ�
���� virus_arr�迭�� ���̷����� ������Ű�� ȸ���ϴ� ������� �ڵ带 �ۼ��Ͽ����ϴ�
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
            if not virus_arr[ny][nx]: #�迭 �ٱ��� ���� �θ��� �ʾҴٸ� 4���� ��Һ� ������ �ʿ������ϴ�
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
                    virus_arr[i][j]=1 #���� virus_arr �迭���� ���� �����ݴϴ�
                    makeWall(cnt+1)
                    arr[i][j]=0 #���� ȸ�����ݴϴ�
                    virus_arr[i][j]=0

def debugging(array):
    for i in range(1,N+1):
        for j in range(1,M+1):
            print(array[i][j],end=" ")
        print()
    print()

makeWall(0)
print(maximum)