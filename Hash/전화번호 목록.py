# 브루트 포스로 하면 O(N^2)이라 시간 초과
# 해시를 이용해서 접두어가 있는지 확인
# key 값이 있는지 체크하는건 O(1) 이라 효율적.

def solution(phone_book):
    d={}
    
    for pn in phone_book:
        d[pn]=True
    
    for pn in phone_book:
        length=len(pn)
        appendix=""
        for i in range(length):
            appendix+=pn[i]
            if appendix in d and appendix!=pn:
                return False
            
    return True