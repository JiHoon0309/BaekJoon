import math
N=int(input())

for i in range(N):
    x,y=map(int,input().split())

    a=round((y-x)**0.5)
    b=math.ceil((y-x)**0.5)
    if a==b:
        print(a+a-1)
    else:
        print(a+a)