for i in range(int(input())):
    string=input()
    K=int(input())
    boundary=K-1
    minimum = float('inf')
    maximum = float('-inf')
    
    arr=[[0] for i in range(26)]
    """
    ���ĺ��� 2���� �迭�� �������ݴϴ�.
    ��� ���� K���� ���ڿ� ��� ��ġ�� �����ϴ��� �迭���� �������ݴϴ�.
    �̶�, 26���� ���� �� �ʿ� ������ 0��° ��ҿ� count���� ���� K�� �̻��� ���ĺ��� Ž���մϴ�.
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
            � ���� K���� ��Ȯ�� �����ؾ��Ҷ� ����ؾ��ϴ� ������ ������ �׻� K�Դϴ�.
            ����(������) ũ�⸸ŭ�� Ž���ϸ� ������ �ű�⸸ �ϸ� �����ϰ� �ذ��� �� �ֽ��ϴ�.
            �̷� ������ ����� �����̵� ������ Ȥ�� �� �����Ͷ� �մϴ�.
            """
    if exist:
        print(minimum+1,maximum+1)
    else:
        print(-1)