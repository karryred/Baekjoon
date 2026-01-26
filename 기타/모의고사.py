def solution(answers):
    correct_cnt=[0,0,0]
    s1=[1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if s1[i%5]==answers[i]:
            correct_cnt[0]+=1
        if s2[i%8]==answers[i]:
            correct_cnt[1]+=1
        if s3[i%10]==answers[i]:
            correct_cnt[2]+=1
        
    max_val=max(correct_cnt)
    answer=[]
    for i in range(0,3):
        if correct_cnt[i]==max_val:
            answer.append(i+1)
        
    return answer