N=int(input())
arr=[1]
i=0
while N>arr[i]:
    arr.append(arr[i]+(i+1)*6)
    i+=1
print(i+1)