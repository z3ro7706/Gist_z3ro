import sys
input=sys.stdin.readline

arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    for j in range(0,i):
        if(arr[i]>=arr[j]):
            arr=arr[0:j]+[arr[i]]+arr[j:i]+arr[i+1:]

print(*arr)