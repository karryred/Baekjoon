N=int(input()) #�ϼ�
time_table=[]
for i in range(N):
    duration,benefit=map(int,input().split())
    time_table.append((duration,benefit))

DP=[0 for i in range(N+1)]

for i in range(N):
    for j in range(i+time_table[i][0],N+1):
        if DP[i]+time_table[i][1]>DP[j]:
            DP[j]=DP[i]+time_table[i][1]
    """
    �� i�� ������ ����� ���մϴ�. �����ϰ� ������ ������ ��, �� i �ݺ����� ����ؾ��� ���� �� ����� �޴��� or ���� �ʴ��� �Դϴ�.
    ���� ����� �޴´ٸ� (i-1)���� �ִ� + �ش� ����� ������ �ִ����� ���ŵ� ���Դϴ�. �̶� ���ŵǴ� ��ġ�� i+�ҿ�Ǵ� �ð��Դϴ�.
    ���⼭ DP[i]+time_table[i][1]�� �ִ� + �����̸� j�� ���ŵǴ� ��¥�Դϴ�.
    ����ؼ� j�� ������Ű�鼭 ���� DP[i]+time_table[i][1]���� ���ϴ� ������ ����� ������ ���� ������ �� �ִ� ��¥�� ���� �Ϸ�� �����Դϴ�.
    ���� 3��°�� 2Ʋ�� �ɸ��� ����� �ִٸ� DP 5��,6�� ... N�� ���� (DP[2]+����)���� ���ϸ� �� �� �Դϴ�.
    """
            
print(DP[-1])