import sys
input=sys.stdin.readline

def LCS(X:list,Y:list,n:int,m:int):
    table=[[0 for _ in range(m+1)]for _ in range(n+1)]
   
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1]==Y[j-1]):
                table[i][j]=table[i-1][j-1]+1
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])

    return table[n][m]

X=list(input())
Y=list(input())

print(LCS(X,Y,len(X)-1,len(Y)-1))