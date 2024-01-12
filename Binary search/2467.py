N=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)

low=0
high=len(arr)-1
res=float('inf')
left=0
right=0

while low<high:
    #sum = arr[low]+arr[high]
    if res>abs(arr[low]+arr[high]):
        res=abs(arr[low]+arr[high])
        left=low
        right=high

    #if sum>0 
    if abs(arr[low])<abs(arr[high]):
        high-=1
    else:
        low+=1
"""
�� ����� ������ ���� ���� sum�� �� ���ο� ����� �󸶳� 0�� ��������� ��Ÿ���ϴ�.
���� sum�� 0�̸��̶�� ��Į������ ġ������ �ִٴ� ���̰� 0 �̻��̶�� �꼺�� ġ������ �ִٴ� �ǹ��Դϴ�.
�� ������ ������� sum�� 0 �̻��� ��� �꼺�� ġ������ �ִٴ� ���̴� �꼺��� ���� �ٿ���� �� ���Դϴ�.
���� �꼺��� ���� ���̱����� right�� �������� �� ĭ �̵��մϴ�.

�̶� �̵��ߴٰ� ������ ���ο� ����� 0�� �� ����� ���� �ƴմϴ�.
ex) -700 -400 -100 800
-700 �� 800�� sum�� 100�̴� �������� �� ĭ �Ű��ݴϴ�.
-700 -100�� sum�� -800�̹Ƿ� 0�� �� �־������ϴ�.
ĭ�� �̵��ϴ� ���� sum�� �پ�� '���ɼ�'�� �����ϴ� ������ ������ �پ��� ���� �ƴ� ���� �������ݽô�.
"""
print(arr[left],arr[right])