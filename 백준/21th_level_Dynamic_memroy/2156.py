import sys
input=sys.stdin.readline

n=int(input())
arr=[]

value_list=[0]*n

for i in range(0,n):
    value=int(input())
    arr.append(value)


if n == 1:
    print(arr[0])
    exit(0)

if n == 2:
    print(arr[0] + arr[1])
    exit(0)
    
if(len(arr)!=n):
    print("input data error")
    exit(0)

value_list[0]=arr[0]
value_list[1]=arr[0]+arr[1]

for i in range(2,n):
    value_list[i]=max(value_list[i-3]+arr[i-1]+arr[i],value_list[i-2]+arr[i],value_list[i-1])

print(max(value_list))

