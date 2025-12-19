import sys
input=sys.stdin.readline

def LCS(X,Y,table):
    n=len(X)
    m=len(Y)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1]==Y[j-1]):
                table[i][j]=table[i-1][j-1]+1
            else:
                table[i][j]=_max(table[i-1][j],table[i][j-1])
    return table[-1][-1]


def _max(x,y):
    if(x>=y):
        return x
    else:
        return y

x=list(input().strip())
y=list(input().strip())

table=[[0 for _ in range(len(y)+1)]for _ in range(len(x)+1)]

print(LCS(x,y,table))