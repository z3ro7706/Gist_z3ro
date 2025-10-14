import sys
input=sys.stdin.readline

x,n=map(int,input().split())

arr=list(map(int,input().split()))

if(len(arr)!= x):
    print("Input data error")
    exit(0)

arr_new=[0]*x
arr_new[0]=arr[0]
for i in range(1,x):
    arr_new[i]=arr_new[i-1]+arr[i]

for i in range(0,n):
    a,b=map(int,input().split())
    if(a==1):
        print(arr_new[b-1])
    else:
        print(arr_new[b-1]-arr_new[a-2])
