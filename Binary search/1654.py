K,N =map(int,input().split())
LAN=[]
for i in range(K):
    LAN.append(int(input()))

low=1
high=max(LAN)

while low<=high:
    cnt=0
    mid=(low+high)//2
    for i in LAN:
        cnt+=i//mid

    if cnt<N:
        high=mid-1
    else:
        low=mid+1

print(high)
"""
이 문제에서 제일 중요한 부분은 high를 출력해주는 부분입니다.
길이를 210으로 잘랐을 때 cnt 값이 10이라 가정하면 너무 길게 자른 거니 최대값으로 사용할 수 없습니다.
그래서 190으로 잘랐을 때 cnt값이 11이라고 해도 이게 정말 최댓값인지 알 수 없습니다.
따라서 cnt값이 동일하더라도 low값을 올려 최대값을 찾아가는 과정이 필요합니다.

이분탐색을 하다 보면 low가 high를 넘긴 순간 종료되는데 이 low가 high를 넘기는 순간은 cnt가 N보다 작아(길이가 길어) high=mid-1을 하는 상황입니다.
계산 후에 low=mid=high+1의 상태가 되어 정답범위는 high이하에 존재하고 그렇다면 최댓값인 high가 정답이 될 것입니다.
"""