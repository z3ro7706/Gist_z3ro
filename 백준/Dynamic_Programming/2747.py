import sys
input=sys.stdin.readline

def Fibonacci(n):
    if(n<=1):
        return 1
    arr=[0]*n
    arr[0]=1
    arr[1]=1
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[-1]

x=int(input().strip())
print(Fibonacci(x))