arr=[]
for i in range(0,9):
    a=int(input())
    arr.append(a)

max_v=arr[0]
count=0
b=1

for i in arr:
    count+=1
    if i>max_v:
        max_v=i
        b=count 

print(max_v)
print(b)