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
�� �˰���� �޸� ��� �� dp[j]�� ���ؼ� Ž���� �����ϱ� ������ ȿ�������� ���մϴ�
���԰� 15��� �ϸ� 15�� ���� ���ڴ� dp[15]�� ������ �ϳ� ���������� dp[p]+1 �ΰ��� ���̽��� �����մϴ�
���� �񱳸� ���� ��ŭ �� dp[n]���� �ϸ� ���� ��� j�� ���ؼ� ���� �ʿ� �����ϴ�
"""

if dp[K]==K+1:
    print(-1)
else:
    print(dp[K])