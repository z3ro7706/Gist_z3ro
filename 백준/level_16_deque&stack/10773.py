x=int(input())
arr=[]
for i in range(0,x):
    n=int(input())
    if(n!=0):
        arr.append(n)
    else:
        arr.pop()

add=0
for i in arr:
    add+=i
print(add)