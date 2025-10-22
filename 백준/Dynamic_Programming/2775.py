import sys
input=sys.stdin.readline

def apart(arr:list,k:int,n:int):
    if(arr[k][n]!=0):
        return arr[k][n]
    
    if(k==0 and n==0):
        return 0
    
    if(k==0):
        return arr[k][n]
    
    if(n<=0):
        arr[k][n]=apart(arr,k-1,n)
        return arr[k][n]
    else:
        arr[k][n]=apart(arr,k-1,n) + apart(arr,k,n-1)
        return arr[k][n]
    


x=int(input())
arr=[[0]*15 for _ in range(0,15)]

for i in range(0,14):
    arr[0][i+1]=i+1

for i in range(0,x):
    k=int(input().strip())
    n=int(input().strip())
    print(apart(arr,k,n))