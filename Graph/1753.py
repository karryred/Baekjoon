import heapq
import sys

input=sys.stdin.readline

def Dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start]=0
    """
    �켱���� ť�� ����Ͽ��� �� ���ͽ�Ʈ�� �˰����� �ð����⵵�� �پ��� ������ ���ʿ��� ������ �پ��� �����Դϴ�.
    A, B, C, D ��尡 �����ϰ� ������ (A,C,3) (B,D,4) (C,D,2) (A,C,7) ��� ��������� �����Ѵٰ� �����غ��ô�.
    �Ϲ� ť�� ��� A -> B -> C -> D ������ ��带 �湮�� ���̰� D�� �Ÿ� ������ 2��(B�� �������ν�, C�� �������ν�) �Ͼ�� �˴ϴ�.
    �̿� ���� �켱���� ť�� ��� A -> C -> D -> B�� ������ �湮�ϸ� D�� �Ÿ� ������ �� �ѹ��� �߻��մϴ�.
    �̴� �켱���� ť�� ������� �ܰ迡�� �ּҰ��� �����ϱ� �����Դϴ�.
    """

    while Q:
        dist,node=heapq.heappop(Q) #Ʃ���� ��� �켱���� ������ �� ��Һ��� �����ϱ� ������ dist(�Ÿ�)�� ������ �;��մϴ�.
        
        if distance[node]<dist:
            continue
        """
        �� �Լ������� �Ÿ��� ���ŵ� ������ ť���ٰ� �ش��ϴ� ���(�Ÿ�,���)�� �־��ݴϴ�.
        ���� �켱���� ť�� ���� ���, �ٸ� �Ÿ��� ���� Ʃ���� ������ �� �ְ� ������ pop �� ���Դϴ�.
        �켱���� ť�� ��� ���� �������� �ʰ� ������ pop�� �Ǵ� ������ ��ȿ�������� ���� ���� ������ �׷��� �ʽ��ϴ�.
        �켱���� ť���� ��� ���� �����Ϸ��� ����-���� ������ ���ľ��ϰ� ������ �켱���� ť�� Ư�� ���п� ������ pop��
        �Ǵ� ��찡 �׸� ���� �ʱ⶧���Դϴ�.
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