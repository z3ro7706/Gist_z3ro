import sys
input=sys.stdin.readline

a=int(input())

arr_length=list(map(int,input().split()))
arr_price=list(map(int,input().split()))

if(len(arr_length)!=(a-1)):
    exit(0)
elif(len(arr_price)!=a):
    exit(0)

min=1000000001
tot=0
for i in range(0,a-1):
    if(arr_price[i]<=min):
        min=arr_price[i]
    tot+=min*arr_length[i]

print(tot)
