N = int(input())
nums = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1) 
"""
{10,20,10,30,20,50} 순열의 최장 부분 순열은 {10,20,10,30,20} 순열의 최장 부분 순열에 50까지 추가해 게산한 값일 것입니다.
이런식으로 sub problem으로 나눠 볼 수 있고 부분 문제의 최적해로 전체 문제의 최적해를 도출해낼 수 있습니다.
만약 숫자의 대소를 비교해보았을 때,
nums[i]가 더 크다면 dp[j]까지의 부분 순열에서 nums[i]를 더해 dp[i]의 부분 순열을 만들 수 있습니다.
이때, 지금의 부분 순열이 더 길 수도 있기 때문에 max값을 dp[i]로 갱신합니다.
"""

print(max(dp))