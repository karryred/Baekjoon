for i in range(int(input())):
    string=input()
    K=int(input())
    boundary=K-1
    minimum = float('inf')
    maximum = float('-inf')
    
    arr=[[0] for i in range(26)]
    """
    알파벳을 2차원 배열로 저장해줍니다.
    어떠한 문자 K개가 문자열 어느 위치에 존재하는지 배열에다 저장해줍니다.
    이때, 26개를 전부 볼 필요 없으니 0번째 요소에 count값을 적어 K개 이상인 알파벳만 탐색합니다.
    """
    for i in range(len(string)):
        p=ord(string[i])-97
        arr[p][0]+=1
        arr[p].append(i)

    
    exist=0
    for i in range(26):
        count = arr[i][0]
        if count>boundary:
            exist=1
            for j in range(1,count-boundary+1):
                minimum = min(minimum,arr[i][j+boundary]-arr[i][j])
                maximum = max(maximum,arr[i][j+boundary]-arr[i][j])
            """
            어떤 문자 K개를 정확히 포함해야할때 계산해야하는 길이의 범위는 항상 K입니다.
            같은(고정된) 크기만큼만 탐색하며 앞으로 옮기기만 하면 수월하게 해결할 수 있습니다.
            이런 느낌의 방식을 슬라이딩 윈도우 혹은 투 포인터라 합니다.
            """
    if exist:
        print(minimum+1,maximum+1)
    else:
        print(-1)