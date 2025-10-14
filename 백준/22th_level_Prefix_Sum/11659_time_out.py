import sys
input=sys.stdin.readline

x,y=map(int,input().split())

arr=list(map(int,input().split()))

if(len(arr)!= x):
    print("Input data error")
    exit(0)

for i in range(0,y):
    a,b=map(int,input().split())
    count=0
    for j in range(a-1,b):
        count=count+arr[j]
    print(count)import sys
input=sys.stdin.readline

x,y=map(int,input().split())

arr=list(map(int,input().split()))

if(len(arr)!= x):
    print("Input data error")
    exit(0)

for i in range(0,y):
    a,b=map(int,input().split())
    count=0
    for j in range(a-1,b):
        count=count+arr[j]
    print(count)