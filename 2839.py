N=int(input())

if N>7:
    if N%5==0:
        print(N//5)
    elif N%5==1:
        print((N-6)//5+(6//3))
    elif N%5==2:
        print((N-12)//5+(12//3))
    elif N%5==3:
        print((N-3)//5+(3//3))
    elif N%5==4:
        print((N-9)//5+(9//3))
if N==4 or N==7:
    print(-1)
if N==3 or N==5:
    print(1)
if N==6:
    print(2)
