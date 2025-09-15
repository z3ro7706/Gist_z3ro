#모든 값을 메모리화 시키면, 메모리 초과가 발생하고, 이를 줄이면 시간초과가 발생하는 예민한 문제이다


import sys
input=sys.stdin.readline

n,k=map(int,input().split())

if(n+k>=2*n-k):
    k=n-k

arr=[0]*(4)

arr[0]=n
for i in range(1,k):
    arr[1]=(n-i)*arr[0]
    arr[0]=arr[1]

arr[2]=1
for i in range(1,k):
    arr[3]=arr[2]*(i+1)
    arr[2]=arr[3]

print((arr[0]//arr[2])%1000000007)