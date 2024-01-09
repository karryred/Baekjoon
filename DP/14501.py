N=int(input()) #일수
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
    각 i는 날마다 상담을 뜻합니다. 간단하게 생각해 보았을 때, 각 i 반복에서 고려해야할 것은 그 상담을 받느냐 or 받지 않느냐 입니다.
    만약 상담을 받는다면 (i-1)날의 최댓값 + 해당 상담의 수익이 최댓값으로 갱신될 것입니다. 이때 갱신되는 위치는 i+소요되는 시간입니다.
    여기서 DP[i]+time_table[i][1]이 최댓값 + 수익이며 j가 갱신되는 날짜입니다.
    계속해서 j를 증가시키면서 오직 DP[i]+time_table[i][1]과만 비교하는 이유는 상담을 받을지 말지 결정할 수 있는 날짜가 오직 하루기 때문입니다.
    만약 3일째에 2틀이 걸리는 상담이 있다면 DP 5일,6일 ... N일 전부 (DP[2]+수익)값과 비교하면 될 것 입니다.
    """
            
print(DP[-1])