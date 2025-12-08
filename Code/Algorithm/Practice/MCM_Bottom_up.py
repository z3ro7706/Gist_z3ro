import sys
input=sys.stdin.readline

def MCM(arr,n):
    m=[[0 for _ in range(n+1)]for _ in range(n+1)]

    for i in range(1,n):
        m[i][i]=0

    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            _min=sys.maxsize

            for k in range(i,j):
                cost=m[i][k]+m[k+1][j]+arr[i-1]*arr[k]*arr[j]

                if(cost<=_min):
                    _min=cost
                    m[i][j]=_min

    return m[1][n-1]

n=int(input()) #matrix 개수
arr=list(map(int,input().split()))

if(len(arr)!=n+1):
    print("Input data error")
    exit(0)


print(MCM(arr,n+1))