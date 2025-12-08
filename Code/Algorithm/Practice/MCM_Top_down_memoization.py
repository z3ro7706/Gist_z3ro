import sys
input=sys.stdin.readline

def MCM(arr:list,i:int,j:int,table:list):
    if(i==j):
        return 0
    
    if(table[i][j]!=-1):
        return table[i][j]

    _min=sys.maxsize

    for k in range(i,j):
        count=MCM(arr,i,k,table)+MCM(arr,k+1,j,table)+arr[i-1]*arr[k]*arr[j]
        if(count<=_min):
            _min=count
            table[i][j]=_min

    return _min

n=int(input()) #matrix 개수
arr=list(map(int,input().split()))

if(len(arr)!=n+1):
    print("Input data error")
    exit(0)


table=[[-1 for _ in range(0,n+2)]for _ in range(0,n+2)]
print(MCM(arr,1,n,table))