A,B=map(int,input().split())
A_reverse=(A//100)+(((A//10)%10)*10)+((A%10)*100)
B_reverse=(B//100)+(((B//10)%10)*10)+((B%10)*100)

if A_reverse>B_reverse:
    print(A_reverse)
else:
    print(B_reverse)