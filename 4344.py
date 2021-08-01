C=int(input())
for i in range(C):
    sum=0
    count=0
    score=list(map(int,input().split()))
    for j in range(score[0]):
        sum+=score[j+1]
    avg=sum/score[0]
    for z in range(score[0]):
        if score[z+1]>avg:
            count+=1
    a=(count/score[0])*100
    print(format(a,".3f")+'%')