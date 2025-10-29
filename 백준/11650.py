import sys
input=sys.stdin.readline




x=int(input())
arr=[]
for i in range(0,x):
    x,y=map(int,input().split())
    arr.append([x,y])

print(arr)