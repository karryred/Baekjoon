import heapq
import sys

input=sys.stdin.readline

def Dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start]=0
    """
    우선순위 큐를 사용하였을 때 다익스트라 알고리즘의 시간복잡도가 줄어드는 이유는 불필요한 연산이 줄어들기 때문입니다.
    A, B, C, D 노드가 존재하고 간선은 (A,C,3) (B,D,4) (C,D,2) (A,C,7) 모두 양방향으로 존재한다고 가정해봅시다.
    일반 큐의 경우 A -> B -> C -> D 순으로 노드를 방문할 것이고 D의 거리 갱신이 2번(B의 인접노드로써, C의 인접노드로써) 일어나게 됩니다.
    이에 비해 우선순위 큐의 경우 A -> C -> D -> B의 순으로 방문하며 D의 거리 갱신이 단 한번만 발생합니다.
    이는 우선순위 큐가 현재까지 단계에서 최소값을 보장하기 때문입니다.
    """

    while Q:
        dist,node=heapq.heappop(Q) #튜플의 경우 우선순위 연산을 앞 요소부터 진행하기 때문에 dist(거리)가 앞으로 와야합니다.
        
        if distance[node]<dist:
            continue
        """
        이 함수에서는 거리가 갱신될 때마다 큐에다가 해당하는 요소(거리,노드)를 넣어줍니다.
        따라서 우선순위 큐에 같은 노드, 다른 거리를 가진 튜플이 존재할 수 있고 여러번 pop 될 것입니다.
        우선순위 큐의 요소 값을 수정하지 않고 여러번 pop이 되는 과정이 비효율적으로 보일 수도 있지만 그렇지 않습니다.
        우선순위 큐에서 요소 값을 수정하려면 삭제-삽입 과정을 거쳐야하고 실제로 우선순위 큐의 특성 덕분에 여러번 pop이
        되는 경우가 그리 많지 않기때문입니다.
        """
        for next in adjGraph[node]:
            v=next[0]
            w=next[1]
            
            if distance[v]>dist+w:
                distance[v]=dist+w
                heapq.heappush(Q,(distance[v],v))
                
V,E = map(int,input().split())
adjGraph=[[] for i in range(V+1)]
distance=[float('INF')]*(V+1)
startVertex=int(input())

for i in range(E):
    u,v,w=map(int,input().split())
    adjGraph[u].append((v,w))

Dijkstra(startVertex)

for i in distance[1:]:
    if i==float('inf'):
        print("INF")
    else:
        print(i)