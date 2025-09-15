#이렇게 깊이탐색으로 가는 경우, 수가 증가할때 time comeplxity가 급증하게 된다


import sys
input=sys.stdin.readline


def check_bitonic(a):
    count=0
    for i in range(0,len(a)-2):
        if(count==0):
            if(a[i]>a[i+1]):
                count+=1
        elif(count==1):
            if(a[i]<a[i+1]):

                return False
    return True




n=int(input())
arr=list(map(int,input().split()))

if(n!=len(arr)): #debug
    print("Input data error")
    exit(0)

d = [1] * n

for i in range(1, n): 
    for j in range(i): 
        if arr[j] < arr[i]: 
            d[i] = max(d[i], d[j] + 1) 
print(d)

print(check_bitonic(arr))

