import heapq
import sys

input=sys.stdin.readline

def Dijkstra(start,Graph):
    Q = []
    heapq.heappush(Q,(0,start))
    distance=[float('INF')]*(V+1)
    distance[start]=0
    
    while Q:
        dist,node=heapq.heappop(Q)
        
        if distance[node]<dist:
            continue
        
        for next in Graph[node]:
            v=next[0]
            w=next[1]
            
            if distance[v]>dist+w:
                distance[v]=dist+w
                heapq.heappush(Q,(distance[v],v))
        
    return distance
    
V,E,X = map(int,input().split())
toAdjGraph=[[] for i in range(V+1)]
backAdjGraph=[[] for i in range(V+1)]
toDistance=[0]*(V+1)
backDistance=[0]*(V+1)

for i in range(E):
    u,v,w=map(int,input().split())
    toAdjGraph[u].append((v,w))
    backAdjGraph[v].append((u,w))

toDistance=Dijkstra(X,toAdjGraph)
backDistance=Dijkstra(X,backAdjGraph)

maximum=-1
for i in range(1,V+1):
    cost=toDistance[i]+backDistance[i]
    maximum=max(maximum,cost)

print(maximum)

"""
그래프를 뒤집었을 때 정점으로 가는 길이 오는 길이 될 수 있다는 점만 확인하면 충분할 것 같습니다.
"""