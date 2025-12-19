import sys
input=sys.stdin.readline

def mcm(arr,table):
    n=len(arr)

    for i in range(0,n):
        table[i][i]=0

    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            _min=sys.maxsize
            for k in range(i,j):
                v=table[i][k]+table[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if(_min>=v):
                    _min=v
            table[i][j]=_min
    return table[1][-1]

arr=list(map(int,input().split()))
table=[[0 for _ in range(len(arr))]for _ in range(len(arr))]
print(mcm(arr,table))
