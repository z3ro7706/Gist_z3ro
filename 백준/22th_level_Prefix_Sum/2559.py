#sliding window protocol

import sys
input=sys.stdin.readline

a,b=map(int,input().split())
arr=list(map(int,input().split()))

part_sum=sum(arr[:b])
ans=part_sum

for i in range(a-b):
    part_sum=part_sum+arr[i+b]-arr[i] #앞에 하나를 빼고 뒤에 하나 더하기
    if(ans<part_sum):
        ans=part_sum
    
print(ans)