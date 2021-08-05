T=int(input())

for i in range(T):
    S=list(input())
    for j in range(2,len(S)):
        print(S[j]*int(S[0]),end="")
    print()