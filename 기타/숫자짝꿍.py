def solution(X, Y):
    arr_x=[0]*10
    arr_y=[0]*10
    answer=""
    
    for x in X:
        arr_x[int(x)]+=1
    for y in Y:
        arr_y[int(y)]+=1
    
    for pos in range(9,-1,-1):
        while(arr_x[pos]>0 and arr_y[pos]>0):
                answer+=str(pos)
                arr_x[pos]-=1
                arr_y[pos]-=1
    if answer=="":
        return "-1"
    elif answer[0]=="0":
        return "0"
    return answer