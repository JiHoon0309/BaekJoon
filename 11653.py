N=int(input())
i=2
while True:
    if N==1:
        break
    elif N//i==1 and N%i==0:
        print(i)
        break
    elif N%i==0:
        print(i)
        N=N//i
    elif N%i!=0:
        i+=1