import sys
input=sys.stdin.readline

N,K = map(int,input().split())
coin=[]
for i in range(N):
    w = int(input())
    coin.append(w)
    
dp = [K+1] * (K+1)
dp[0]=0

for i in range(K+1):
    for j in range(N):
        if i-coin[j]>-1 and dp[i-coin[j]]+1<dp[i]:
            dp[i]=dp[i-coin[j]]+1
"""
for i in range(1, K+1) :
    for j in range(i) :
        for p in range(N):
            if i==j+coin[p]:
                dp[i] = min(dp[j]+1,dp[i])
위 알고리즘과 달리 모든 전 dp[j]에 대해서 탐색을 진행하기 때문에 효율적이지 못합니다
무게가 15라고 하면 15와 비교할 숫자는 dp[15]와 코인을 하나 더했을때의 dp[p]+1 두가지 케이스만 존재합니다
따라서 비교를 코인 만큼 뺀 dp[n]과만 하면 되지 모든 j에 대해서 비교할 필요 없습니다
"""

if dp[K]==K+1:
    print(-1)
else:
    print(dp[K])