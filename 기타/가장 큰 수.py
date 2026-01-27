# 애는 학습용이라고 생각하자.
# 맨 앞을 기준으로 정렬한다 => 문자열로 정렬한다

def solution(numbers):
    # 1. 모든 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 2. 각 문자열을 3번 반복한 값을 기준으로 내림차순 정렬
    # (원소가 1000 이하이므로 3번 반복하면 자릿수가 맞춰져 비교 가능)
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 3. 정렬된 숫자들을 이어 붙임
    answer = ''.join(numbers)
    
    # 4. 예외 처리: 모든 숫자가 0인 경우 "000"이 아닌 "0"을 리턴
    return str(int(answer))

def solution(numbers):
    length=len(numbers)
    
    for i in range(1, len(numbers)):
        val=numbers[i]
        pos=i
        for j in range(i-1,0-1,-1):
            pro_j=numbers[j]
            pro_val=val
            while(not 1000<=pro_j<=10000):
                pro_j*=10
            while(not 1000<=pro_val<=10000):
                pro_val*=10
            
            if pro_j<pro_val: # 오름차순 # 이거를 1000단위로 만들어서.
                pos=j
                numbers[j+1]=numbers[j]
        numbers[pos]=val
            
            
    answer=""
    for val in numbers:
        answer+=str(val)
    
    return answer