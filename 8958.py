N=int(input())

for i in range(N):
    score=0
    sum=0
    arr=list(input())
    for j in range(len(arr)):
        if arr[j]=="O":
            score+=1
            sum+=score
        else:
            score=0

    print(sum)