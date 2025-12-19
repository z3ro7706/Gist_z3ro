import sys
input=sys.stdin.readline

def MCM(arr:list,table:list,table_p:list):
    n=len(arr)
    for i in range(0,n):
        table[i][i]=0

    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            v=sys.maxsize
            for k in range(i,j):
                c=table[i][k]+table[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if(v>=c):
                    v=c
                    table_p[i][j]=k
            table[i][j]=v

    return table_p

arr=list(map(int,input().split()))

table=[[ 0 for _ in range(0, len(arr))]for _ in range(0,len(arr))]
table_p=[[ 0 for _ in range(0, len(arr))]for _ in range(0,len(arr))]
print(*MCM(arr,table,table_p),sep='\n')