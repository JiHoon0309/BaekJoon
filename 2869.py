import math
A,B,V=map(int,input().split())
C=0

N=math.ceil((V-A)/(A-B))
print(N+1)