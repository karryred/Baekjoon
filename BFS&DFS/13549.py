import queue
import sys

input=sys.stdin.readline

def BFS(N,K):
    Q = queue.Queue()
    Q.put((N,0))
    
    while not Q.empty():
        p,t=Q.get()
        if p==K:
            print(t)
            break
        if 2*p<limit and visited[2*p]==0:
            Q.put((2*p,t))
            visited[2*p]=1
        if visited[p-1]==0 and p>0:
            visited[p-1]=1
            Q.put((p-1,t+1))
        if p+1<limit and visited[p+1]==0:
            Q.put((p+1,t+1))
            visited[p+1]=1

"""
        if p+1<limit and visited[p+1]==0:
            Q.put((p+1,t+1))
            visited[p+1]=1
        if visited[p-1]==0 and p>0:
            visited[p-1]=1
            Q.put((p-1,t+1))

        4 6 �ݷ� ���̽��� �����մϴ�
        4 > 5 > 6�� 4 > 3> 6 ���� 6�� ���� �����Ͽ� visited �� �� ���� ���������µ�
        �̸� �ذ��ϱ� ���ؼ� ���� ������ �����ؾ��մϴ�
"""
N,K = map(int,input().split())
limit=100001
visited=[0]*limit
#��� �ð��� ���̱� ���� �湮ó���� �� �ʿ� ���� ����� �������־�� �մϴ�

if N>=K:
    print(N-K)
else:
    BFS(N,K)