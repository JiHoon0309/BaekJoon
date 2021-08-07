arr=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
N=list(input())
sum=0
for i in range(len(arr)):
    for j in range(len(N)):
        if N[j] in arr[i]:
            sum+=i+3
print(sum)