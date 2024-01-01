import queue
import sys

input=sys.stdin.readline

def BFS(N,K):
    Q = queue.Queue()
    Q.put((N,0))
    
    while not Q.empty():
        p,t=Q.get()
        if p==K:
            print(t)
            break
        if 2*p<limit and visited[2*p]==0:
            Q.put((2*p,t))
            visited[2*p]=1
        if visited[p-1]==0 and p>0:
            visited[p-1]=1
            Q.put((p-1,t+1))
        if p+1<limit and visited[p+1]==0:
            Q.put((p+1,t+1))
            visited[p+1]=1

"""
        if p+1<limit and visited[p+1]==0:
            Q.put((p+1,t+1))
            visited[p+1]=1
        if visited[p-1]==0 and p>0:
            visited[p-1]=1
            Q.put((p-1,t+1))

        4 6 반례 케이스가 존재합니다
        4 > 5 > 6이 4 > 3> 6 보다 6에 먼저 접근하여 visited 할 수 없게 만들어버리는데
        이를 해결하기 위해서 갱신 조건을 수정해야합니다
"""
N,K = map(int,input().split())
limit=100001
visited=[0]*limit
#계산 시간을 줄이기 위해 방문처리를 해 필요 없는 계산을 제외해주어야 합니다

if N>=K:
    print(N-K)
else:
    BFS(N,K)