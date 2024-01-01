import queue

def bfs ():
    while not Q.empty():
        x,y = Q.get()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if -1<nx<rows and -1<ny<cols and adjList[nx][ny]==0:
                adjList[nx][ny] = adjList[x][y]+1
                """
                BFS&DFS���� �ش� ��� ���� �÷��ݴϴ�.
                �湮ó���� �� ���� �ʿ��� ����(�Ÿ�,�ϼ�) ����� ����� �� �ֽ��ϴ�.
                ���� ���� ���Եǰ� �߿��� �κ��Դϴ�.
                """
                Q.put((nx,ny))
    
dx=[0,0,1,-1] #right left bottom top
dy=[1,-1,0,0]
cols,rows = map(int,input().split())
adjList=[]

for i in range(rows):
    adjList.append(list(map(int, input().split()))) 
    # readline�� ��� �� �ڿ� '\n'���� �Է¹����Ƿ� ��������� ��

Q = queue.Queue()
for i in range(rows):
    for j in range(cols):
        if adjList[i][j]==1:
            Q.put((i,j))

bfs()

cnt=-1
for i in range(rows):
    for j in range(cols):
        if adjList[i][j]==0:
            print(-1)
            exit() #exit�� ����ؼ� �׳� ���α׷��� �ٷ� ������ѹ��� �� ���� ���� �ֽ��ϴ�.
        else:
            cnt = max(cnt,adjList[i][j])

print(cnt-1)