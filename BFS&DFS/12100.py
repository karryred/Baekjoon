import copy

N=int(input())
arrangement=[]
dx=[-1,0,1]
dy=[-1,0,1]
maximum=0

for i in range(N):
    arrangement.append(list(map(int,input().split())))
    temp=max(arrangement[i])
    if temp>maximum:
        maximum=temp

 """
이 문제에서는 5*5*5*5*5의 이동 경로 중 최대값을 찾아야합니다.
한 시점의 board 상태에서 다섯 가지의 이동이 가능하기 때문에 배열 원본을 유지해야합니다.
이를 위해 Deep Copy(깊은 복사)를 사용합니다.
얕은 복사는 배열 객체의 주소값을 복사하여 배열 원본을 유지할 수 없는 바에 비해 깊은 복사는 참조된 객체 자체를 복사하기에
원본 배열에 영향을 끼치지 않습니다.
"""
def move(direction,count,arr):
    
    match direction:
        case 1:
            count+=1
            new_arr=copy.deepcopy(arr) #참조하는 객체의 배열을 복사하여 새로운 객체에 할당한다
            new_arr=moveLeft(new_arr) #해당 배열을 move하고 난 뒤 배열 상태를 할당해준다
            if count!=5:
                for i in range(1,5):
                    move(i,count,new_arr)

        case 2:
            count+=1
            new_arr=copy.deepcopy(arr)
            new_arr=moveRight(new_arr)    
            if count!=5:
                for i in range(1,5):
                    move(i,count,new_arr)

        case 3:
            count+=1
            new_arr=copy.deepcopy(arr)
            new_arr=moveTop(new_arr)
            if count!=5:
                for i in range(1,5):
                    move(i,count,new_arr)

        case 4:
            count+=1
            new_arr=copy.deepcopy(arr)
            new_arr=moveBottom(new_arr)
            if count!=5:
                for i in range(1,5):
                    move(i,count,new_arr)

def moveLeft(arr):
    x=dx[0]
    global maximum

    for i in range(N):
        occur=[]
        for j in range(1,N):
            if arr[i][j]==0: #해당 칸이 0일 경우 계산의 효율성을 위해 스킵한다
                continue
            pos=j
            while pos>0:
                if arr[i][pos+x] == arr[i][pos] and pos not in occur and pos+x not in occur: #합산할 칸 혹은 합산되는 칸 둘 중 하나라도 이미 occur에 들어가 있다면 다시금 합산할 수 없다
                    arr[i][pos+x]*=2
                    arr[i][pos]=0
                    occur.append(pos+x) #합산이 발생한 경우 기록
                    if maximum<arr[i][pos+x]: #합산이 발생할 경우에는 최대값을 갱신할 가능성이 있으니 계산해준다
                        maximum = arr[i][pos+x]
                        #debugging(arr)
                elif arr[i][pos+x] == 0:
                    arr[i][pos+x] = arr[i][pos]
                    arr[i][pos]=0
                else:
                    pass
                pos=pos-1
                
    return arr

def moveRight(arr):
    x=dx[2]
    global maximum
    
    for i in range(N):
        occur=[]
        for j in range(N-2,-1,-1):
            if arr[i][j]==0: #해당 칸이 0일 경우 계산의 효율성을 위해 스킵
                continue
            pos=j
            while pos<N-1:
                if arr[i][pos+x] == arr[i][pos] and pos not in occur and pos+x not in occur:
                    arr[i][pos+x]*=2
                    arr[i][pos]=0
                    occur.append(pos+x) #합산이 발생한 경우 기록 
                    if maximum<arr[i][pos+x]:
                        maximum=arr[i][pos+x]
                elif arr[i][pos+x] == 0:
                    arr[i][pos+x] = arr[i][pos]
                    arr[i][pos]=0
                else:
                    pass
                pos=pos+1
                
    return arr

def moveTop(arr):
    y=dy[0]
    global maximum
    
    for i in range(N):
        occur=[]
        for j in range(1,N):
            if arr[j][i]==0: #해당 칸이 0일 경우 계산의 효율성을 위해 스킵
                continue
            pos=j
            while pos>0:
                if arr[pos+y][i] == arr[pos][i] and pos not in occur and pos+y not in occur:
                    arr[pos+y][i]*=2
                    arr[pos][i]=0
                    occur.append(pos+y) #합산이 발생한 경우 기록
                    if maximum<arr[pos+y][i]:
                        maximum=arr[pos+y][i]
                elif arr[pos+y][i] == 0:
                    arr[pos+y][i] = arr[pos][i]
                    arr[pos][i]=0
                else:
                    pass
                pos=pos-1
                
    return arr

def moveBottom(arr):
    y=dy[2]
    global maximum
    
    for i in range(N):
        occur=[]
        for j in range(N-2,-1,-1):
            if arr[j][i]==0: #해당 칸이 0일 경우 계산의 효율성을 위해 스킵
                continue
            pos=j
            while pos<N-1:
                if arr[pos+y][i] == arr[pos][i] and pos not in occur and pos+y not in occur:
                    arr[pos+y][i]*=2
                    arr[pos][i]=0
                    occur.append(pos+y) #합산이 발생한 경우 기록
                    if maximum<arr[pos+y][i]:
                        maximum=arr[pos+y][i]
                elif arr[pos+y][i] == 0:
                    arr[pos+y][i] = arr[pos][i]
                    arr[pos][i]=0
                else:
                    pass
                pos=pos+1
                
    return arr

def debugging(arr):
    print("-----------------")
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=" ")
        print()

for i in range(1,5):
    move(i,0,arrangement)

print(maximum)
