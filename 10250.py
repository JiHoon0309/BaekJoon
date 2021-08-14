T=int(input())
for i in range(T):
    arr=[]
    H,W,N=map(int,input().split())
    for j in range(1,W+1):
        a=format(j,"02")
        for z in range(1,H+1):
            arr.append(f"{z}{a}")
        
        
    print(arr[N-1])