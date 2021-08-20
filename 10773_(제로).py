import sys
input=sys.stdin.readline
K=int(input())
arr=[]

for i in range(K):
    N=int(input())
    if N!=0:
        arr.append(N)
    else:
        arr.pop()

print(sum(arr))