N=int(input())
count=0
for i in range(N):
    new=[]
    word=list(input())
    new.append(word[0])
    for j in range(1,len(word)):
        if word[j-1]==word[j]:
            continue
        else:
            new.append(word[j])
    
    wordset=set(new)
    if len(wordset)==len(new):
        count+=1
    else:
        continue

print(count)