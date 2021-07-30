N=int(input())
score=list(map(int,input().split()))
result_1=0

for i in range(0,N):
    result=score[i]/max(score)*100
    result_1+=result

print(result_1/N)