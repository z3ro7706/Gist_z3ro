import sys
input=sys.stdin.readline

def mcm(arr,i,j,m):
    if(i==j):
        return 0
    
    if(m[i][j]!=-1):
        return m[i][j]
    else:
        _min=sys.maxsize
        for k in range(i,j):
            v=mcm(arr,i,k,m)+mcm(arr,k+1,j,m)+arr[i-1]*arr[k]*arr[j]
            if(_min>=v):
                _min=v
            
        m[i][j]=_min
        return m[i][j]
    
arr=list(map(int,input().split()))
m=[[-1 for _ in range(len(arr))]for _ in range(len(arr))]
print(mcm(arr,1,len(arr)-1,m))