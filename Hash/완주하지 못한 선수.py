def solution(participant, completion):
    d={}
    
    for p in participant:
        d[p] = d.get(p,0)+1
    
    for p in completion:
        d[p]= d.get(p,0)-1
    
    for key,value in d.items():
        if value!=0:
            answer=key
            break
    
    return answer