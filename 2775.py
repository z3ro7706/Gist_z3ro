import sys
input=sys.stdin.readline

def apart(arr:list,k:int,n:int):
    if(arr[k][n]!=0):
        return arr[k][n]
    
    return apart(arr,)
    

    

x=int(input())
arr=[[0]*14 for _ in range(0,14)]

for i in range(0,14):
    arr[0][i]=i

for i in range(0,x):
    k=int(input())
    n=int(input())
    print(apart(arr,k,n))