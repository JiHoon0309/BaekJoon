Word=list(input().upper())
Alphabet=list("ABCDEFGHIJKLMNOPQRUSUVWXYZ")
count=0
S=0
for i in range(len(Word)):
    arr=[0]*len(Alphabet)

    if Word[i]==Alphabet[0]:
        count+=1

arr[0]=count
print(arr)