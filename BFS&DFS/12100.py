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
�� ���������� 5*5*5*5*5�� �̵� ��� �� �ִ밪�� ã�ƾ��մϴ�.
�� ������ board ���¿��� �ټ� ������ �̵��� �����ϱ� ������ �迭 ������ �����ؾ��մϴ�.
�̸� ���� Deep Copy(���� ����)�� ����մϴ�.
���� ����� �迭 ��ü�� �ּҰ��� �����Ͽ� �迭 ������ ������ �� ���� �ٿ� ���� ���� ����� ������ ��ü ��ü�� �����ϱ⿡
���� �迭�� ������ ��ġ�� �ʽ��ϴ�.
"""
def move(direction,count,arr):
    
    match direction:
        case 1:
            count+=1
            new_arr=copy.deepcopy(arr) #�����ϴ� ��ü�� �迭�� �����Ͽ� ���ο� ��ü�� �Ҵ��Ѵ�
            new_arr=moveLeft(new_arr) #�ش� �迭�� move�ϰ� �� �� �迭 ���¸� �Ҵ����ش�
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
            if arr[i][j]==0: #�ش� ĭ�� 0�� ��� ����� ȿ������ ���� ��ŵ�Ѵ�
                continue
            pos=j
            while pos>0:
                if arr[i][pos+x] == arr[i][pos] and pos not in occur and pos+x not in occur: #�ջ��� ĭ Ȥ�� �ջ�Ǵ� ĭ �� �� �ϳ��� �̹� occur�� �� �ִٸ� �ٽñ� �ջ��� �� ����
                    arr[i][pos+x]*=2
                    arr[i][pos]=0
                    occur.append(pos+x) #�ջ��� �߻��� ��� ���
                    if maximum<arr[i][pos+x]: #�ջ��� �߻��� ��쿡�� �ִ밪�� ������ ���ɼ��� ������ ������ش�
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
            if arr[i][j]==0: #�ش� ĭ�� 0�� ��� ����� ȿ������ ���� ��ŵ
                continue
            pos=j
            while pos<N-1:
                if arr[i][pos+x] == arr[i][pos] and pos not in occur and pos+x not in occur:
                    arr[i][pos+x]*=2
                    arr[i][pos]=0
                    occur.append(pos+x) #�ջ��� �߻��� ��� ��� 
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
            if arr[j][i]==0: #�ش� ĭ�� 0�� ��� ����� ȿ������ ���� ��ŵ
                continue
            pos=j
            while pos>0:
                if arr[pos+y][i] == arr[pos][i] and pos not in occur and pos+y not in occur:
                    arr[pos+y][i]*=2
                    arr[pos][i]=0
                    occur.append(pos+y) #�ջ��� �߻��� ��� ���
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
            if arr[j][i]==0: #�ش� ĭ�� 0�� ��� ����� ȿ������ ���� ��ŵ
                continue
            pos=j
            while pos<N-1:
                if arr[pos+y][i] == arr[pos][i] and pos not in occur and pos+y not in occur:
                    arr[pos+y][i]*=2
                    arr[pos][i]=0
                    occur.append(pos+y) #�ջ��� �߻��� ��� ���
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
