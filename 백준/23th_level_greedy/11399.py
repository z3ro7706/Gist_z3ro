import sys
input=sys.stdin.readline

case=int(input())
arr=list(map(int,input().split()))

arr.sort(reverse=False)

for i in range(1,case):
    arr[i]=arr[i-1]+arr[i]

count=0

for i in arr:
    count+=i

print(count)