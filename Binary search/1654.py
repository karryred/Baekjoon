K,N =map(int,input().split())
LAN=[]
for i in range(K):
    LAN.append(int(input()))

low=1
high=max(LAN)

while low<=high:
    cnt=0
    mid=(low+high)//2
    for i in LAN:
        cnt+=i//mid

    if cnt<N:
        high=mid-1
    else:
        low=mid+1

print(high)
"""
�� �������� ���� �߿��� �κ��� high�� ������ִ� �κ��Դϴ�.
���̸� 210���� �߶��� �� cnt ���� 10�̶� �����ϸ� �ʹ� ��� �ڸ� �Ŵ� �ִ밪���� ����� �� �����ϴ�.
�׷��� 190���� �߶��� �� cnt���� 11�̶�� �ص� �̰� ���� �ִ����� �� �� �����ϴ�.
���� cnt���� �����ϴ��� low���� �÷� �ִ밪�� ã�ư��� ������ �ʿ��մϴ�.

�̺�Ž���� �ϴ� ���� low�� high�� �ѱ� ���� ����Ǵµ� �� low�� high�� �ѱ�� ������ cnt�� N���� �۾�(���̰� ���) high=mid-1�� �ϴ� ��Ȳ�Դϴ�.
��� �Ŀ� low=mid=high+1�� ���°� �Ǿ� ��������� high���Ͽ� �����ϰ� �׷��ٸ� �ִ��� high�� ������ �� ���Դϴ�.
"""