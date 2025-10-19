arr=[]
for i in range(0,30):
    arr.append(0) #0으로 가득찬 list 생성


for i in range(0,28):
    a=int(input())
    arr[a-1] = 1

for i in range(len(arr)):
    if(arr[i]==0):
        print(i+1)