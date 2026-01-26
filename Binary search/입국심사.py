# 솔직히 이 문제를 이분탐색으로 풀려고 떠올리는건 쉽지 않음.
# 다음에도 이분탐색으로 풀 수 있는 문제인지 체크해보기 위해선
# 1. 결정 문제로 바꿀 수 있는가?
# 최적의 값을 찾는 대신, 'X라는 값으로 이게 가능해?'라고 물었을 때 답하기 쉬운가?
# 2. 단조성(Monotonicity)이 있는가?
# 값이 커진다고 결과가 바뀌는 일은 없어야함.

# 이진탐색 low<=high, mid+1, mid-1 기억. 매번 헷갈림
# low==high는 값이 같은 경우의 mid 값을 검사하기 위해서 꼭 필요
# +1 -1은 위치를 옮기기 위해서 필요

def solution(n, times):
    low = 0
    high = max(times)*n
    mid = (low+high)//2
    
    while low<=high:
        sum=0
        for time in times:
            sum += mid//time 
        
        if sum>=n:
            answer=mid # 최대 최소 찾는 이진 탐색 문제는 이렇게 값 저장해두기.
            high = mid-1 
        else:
            low = mid+1 
            
        mid = (low+high)//2 
        
    return answer