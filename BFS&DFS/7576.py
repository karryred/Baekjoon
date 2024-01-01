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
                BFS&DFS에서 해당 요소 값을 올려줍니다.
                방문처리와 그 외의 필요한 값들(거리,일수) 등등을 기록할 수 있습니다.
                정말 많이 쓰게되고 중요한 부분입니다.
                """
                Q.put((nx,ny))
    
dx=[0,0,1,-1] #right left bottom top
dy=[1,-1,0,0]
cols,rows = map(int,input().split())
adjList=[]

for i in range(rows):
    adjList.append(list(map(int, input().split()))) 
    # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

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
            exit() #exit를 사용해서 그냥 프로그램을 바로 종료시켜버릴 수 버릴 수도 있습니다.
        else:
            cnt = max(cnt,adjList[i][j])

print(cnt-1)