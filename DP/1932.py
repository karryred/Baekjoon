"""
본래 1차원 배열로 이 문제를 풀이하려 했으나,
2진트리가 아니라서 1차원 배열로 DP를 구성할 수 없거나 어려움.

또한 2차원 형태로 input이 주어지기도하니 2차원 배열로 풀이 가닥을 잡기

"""
n = int(input())
dp = [[0]*n for i in range(n)]

for i in range(n):
    dp[i]=list(map(int, input().split()))
    
for i in range(1,n):
    for j in range(n):
        if j-1>=0 and j<i:
            dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])
        elif j-1<0:
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]

print(max(dp[n-1]))