#time complexity가 O(n^2) 이므로 시간 초과가 발생

import sys
input=sys.stdin.readline

a,b=map(int,input().split())

arr=list(map(int,input().split()))

calculate=[0]*a

calculate[0]=arr[0]
for i in range(1,a):
    calculate[i]=calculate[i-1]+arr[i]

count=0
for i in calculate:
    if(i%b==0):
        count+=1


for i in range(0,a):
    for j in range(i+1,a):
        if((calculate[j]-calculate[i])%b==0):#나눈 나머지가 0 이라면
            count+=1

print(count)
