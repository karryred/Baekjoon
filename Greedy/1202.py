import heapq
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
jewel=[]
for i in range(N):
    M,V=map(int,input().split())
    heapq.heappush(jewel,(M,-V))

bag=[]
for i in range(K):
    capacity=int(input())
    bag.append(capacity)
bag=sorted(bag)
total=0
candidate=[]

for i in bag:
    limit=i+1
    while jewel and limit>jewel[0][0]:
        heapq.heappush(candidate,heapq.heappop(jewel)[1])
    if candidate:
        total+=heapq.heappop(candidate)
"""
�ڷᱸ���� heap�� ����ϱ� ������ �� ���� ��Ұ� �ּҰ��Դϴ�.
while������ ���԰� limit�� ������� �ʴ��� Ȯ���� �� pop���� candidate(�ĺ���)���� �־��ݴϴ�.
while���� ���԰� limit�� �Ѿ ������ ����˴ϴ�. �̴� �ش� ������ ������ �� �ִ� ��� �������� �ĺ����� �߰��ϴ� �����Դϴ�.
�߰��� �ĺ��� ��, ���� ������ ���� ������ �̾Ƴ��ϴ�. �� �������� ���� ���������� ����� �����̱� ������ �׳� ���� ��ġ�� ���� ������ �̾��ָ� �˴ϴ�.
��� ���濡 ���ؼ� �� ������ �ݺ��մϴ�.
"""
print(-total)