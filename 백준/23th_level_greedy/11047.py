import sys
input = sys.stdin.readline

n,k=map(int,input().split())
arr=[]
for i in range(0,n):
    value=int(input())
    if(k>=value):
        arr.append(value)

line=len(arr)
count=0
price=k
for i in range(0,line):
    if(price==0):
        break
    elif(price<0):
        print("Coin error")
        break

    count+=(price//arr[line-i-1])
    price=price-arr[line-i-1]*(price//arr[line-i-1])

print(count)