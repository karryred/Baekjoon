"""
일반적인 문제와 달리 순서가 다른 구성일지라도 같은 경우의 수로 간주한다는 점.

DP문제에서 규칙을 찾기 힘들다면 점화식을 직접 작성해보면서 규칙을 찾아가는 것 또한 방법
"""

n, target = map(int, input().split())

dp = [0]*(target+1)
dp[0]=1
coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort()

for coin in coins:
    for i in range(target+1):
        if i-coin>=0:
            dp[i]+=dp[i-coin]
            
print(dp[target])