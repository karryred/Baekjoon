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
두 용액을 합쳤을 때의 값인 sum은 이 새로운 용액이 얼마나 0에 가까운지를 나타냅니다.
만약 sum이 0미만이라면 알칼리성에 치우쳐져 있다는 뜻이고 0 이상이라면 산성에 치우쳐져 있다는 의미입니다.
이 생각을 기반으로 sum이 0 이상인 경우 산성에 치우쳐져 있다는 것이니 산성용액 값을 줄여줘야 할 것입니다.
따라서 산성용액 값을 줄이기위해 right을 왼쪽으로 한 칸 이동합니다.

이때 이동했다고 무조건 새로운 용액이 0에 더 가까운 것은 아닙니다.
ex) -700 -400 -100 800
-700 과 800의 sum은 100이니 왼쪽으로 한 칸 옮겨줍니다.
-700 -100의 sum은 -800이므로 0과 더 멀어졌습니다.
칸을 이동하는 것은 sum이 줄어들 '가능성'이 존재하는 것이지 무조건 줄어드는 것이 아닌 점을 주의해줍시다.
"""
print(arr[left],arr[right])