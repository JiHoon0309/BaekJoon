N=int(input())
count=1
new=N

while True:
    A=int(new/10)
    B=int(new%10)
    sum=A+B
    new=(B*10)+(sum%10)
    if new == N:
        break
    else:
        count+=1

print(count)