#Time Complexity = O(2^n)
import sys
input=sys.stdin.readline

def MCM(arr:list,i:int,j:int,table:int):
    if(i==j):
        return 0
    
    v=sys.maxsize
    for k in range(i,j):
        mcm=MCM(arr,i,k,table)+MCM(arr,k+1,j,table)+arr[i-1]*arr[k]*arr[j]
        if(v>=mcm):
            v=mcm

    table[i][j]=v
    return v
    

x=list(map(int,input().split()))
table=[[-1 for _ in range(len(x))]for _ in range(len(x))]
print(MCM(x,1,len(x)-1,table))
