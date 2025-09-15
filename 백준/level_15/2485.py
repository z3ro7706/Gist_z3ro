def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a

x=int(input())
arr=[]
for i in range(0,x):
    arr.append(int(input()))
    
gap=[]
for i in range(0,x-1):
    gap.append(arr[i+1]-arr[i])

value=gap[0]


for i in range(0,x-1):
    value=GCD(gap[i],value)
    
count=0
for i in range(0,x-1):
    count=count+(gap[i]//value)-1

print(count)