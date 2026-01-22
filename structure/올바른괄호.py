def solution(s):
    queue=[]
    
    for pos in s:
        try:
            if pos=='(':
                queue.append('(')
            else:
                queue.pop()
        except:
            return False

    if queue:
        return False
    else:
        return True