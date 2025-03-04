T=int(input())

for i in range(T):
    num = int(input())
    dp=[0]*(num+1)
    dp[0]=1
    #1을 만드는 경우 > 2를 만드는 경우(1에서 2로 0에서 2로)
    for j in range(1,num+1):
        for val in range(1,3+1):
            if j-val>=0:
                dp[j]+=dp[j-val]
    print(dp[num])