import queue

N=int(input()) #크기
K=int(input()) #사과
board=[[0]*N for i in range(N)]
board[0][0]=1
for i in range(K):
    row,column=map(int,input().split())
    board[row-1][column-1]=2

L=int(input()) #전환
rotate=[]
for i in range(L):
    t,d=input().split()
    rotate.append((int(t),d))
rotate.append((10000,""))
    
direction=[(0,1),(1,0),(0,-1),(-1,0)]
Q=queue.Queue()
Q.put((0,0))

def move(board,cnt,time,h,i,j):
    dx=direction[h][0]
    dy=direction[h][1]
    i=i
    j=j
    while(cnt<rotate[time][0]):
        if i+dx<0 or i+dx>N-1 or j+dy<0 or j+dy>N-1 or board[i+dx][j+dy]==1:
            """
            for p in range(N):
                print()
                for q in range(N):
                    print(board[p][q],end=" ")
            """
            return cnt+1
        elif board[i+dx][j+dy]==0:
            board[i+dx][j+dy]=1
            a,b=Q.get()
            board[a][b]=0
            Q.put((i+dx,j+dy))
        else:
            board[i+dx][j+dy]=1
            Q.put((i+dx,j+dy))
        """
        큐를 이용하여 꼬리와 헤드를 관리해주었습니다.
        만약 사과를 만난다면 큐에 삽입만 해주고 그냥 이동할시엔 꼬리를 삭제 후 머리를 삽입해줍니다.
        """
        i+=dx
        j+=dy
        cnt+=1
    
    if rotate[time][1]=='D':
        h=h+1
        if h>3:
            h=0
        #(h+1)%4
    else:
        h=h-1
        if h<0:
            h=3
        #(h-1)%4
    return move(board,cnt,time+1,h,i,j)
    
    
res=move(board,0,0,0,0,0)
print(res)