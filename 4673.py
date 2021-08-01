def self_num(n):
    for i in str(n):
        n+=int(i)
    return n

arr=[]
for i in range(1,10001):
    arr.append(self_num(i))

for i in range(1,10001):
    if i in arr:
        pass
    else:
        print(i)