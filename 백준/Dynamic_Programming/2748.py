import sys
input=sys.stdin.readline

def fibonacci(arr,n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    
    if(arr[n-1]==-1):
        arr[n-1]=fibonacci(arr,n-1)

    if(arr[n-1]==-1):
        arr[n-2]=fibonacci(arr,n-2)
    
    return arr[n-1]+arr[n-2]


x=int(input().strip())
arr=[-1]*(x+2)
print(fibonacci(arr,x+2))