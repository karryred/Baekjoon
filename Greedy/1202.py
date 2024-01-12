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
자료구조로 heap을 사용하기 때문에 맨 앞의 요소가 최소값입니다.
while문에서 무게가 limit에 위배되지 않는지 확인한 후 pop시켜 candidate(후보군)힙에 넣어줍니다.
while문은 무게가 limit을 넘어갈 때까지 진행됩니다. 이는 해당 가방이 감당할 수 있는 모든 보석들을 후보군에 추가하는 과정입니다.
추가된 후보군 중, 가장 가격이 높은 보석을 뽑아냅니다. 이 보석들은 전부 무게제약을 통과한 보석이기 때문에 그냥 가장 가치가 높은 보석을 뽑아주면 됩니다.
모든 가방에 대해서 이 과정을 반복합니다.
"""
print(-total)