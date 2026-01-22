def solution(record):
    
    user_info={}
    
    for log in record:
        if log[0:5]=="Leave":
            continue
        words=log.split()
        user_info[words[1]] = words[2] # 유저 아이디 : 닉네임 -> 최종 일관성 보장
    
    answer=[]
    for log in record:
        if log[0:5]=="Enter":
            words=log.split()
            if words[1] in user_info:
                log = f"{user_info[words[1]]}님이 들어왔습니다."
            else:
                log = f"{words[2]}님이 들어왔습니다."
            answer.append(log)
        
        elif log[0:5]=="Leave":
            words=log.split()
            log = f"{user_info[words[1]]}님이 나갔습니다."     
            answer.append(log)
        
    return answer