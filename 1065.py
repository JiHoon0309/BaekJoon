N=int(input())
count=0
for i in range(1,N+1):
    if i<100:
        count+=1
    if i>100:
        if (i%10)-((i//10)%10)==((i//10)%10)-(i//100):
            count+=1
print(count)