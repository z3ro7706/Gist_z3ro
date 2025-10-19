import sys
input=sys.stdin.readline
from collections import deque

x=int(input())
arr=deque([])
for i in range(1,x+1):
    arr.append(i)

while(1):
    if(len(arr)==1):
        break
    arr.popleft()
    value=arr[0]
    arr.popleft()
    arr.append(value)
    

print(*arr)