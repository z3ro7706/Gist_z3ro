import sys
input=sys.stdin.readline

def LCS(X:list,Y:list,n:int,m:int,table:list):
    if(n==0 or m==0):
        return 0
    
    if(table[n][m]!=-1):
        return table[n][m]
    
    else:
        if(X[n-1]==Y[m-1]):
            table[n][m]=LCS(X,Y,n-1,m-1,table)+1
            return table[n][m]
        else:
            table[n][m]=max(LCS(X,Y,n-1,m,table),LCS(X,Y,n,m-1,table))
            return table[n][m]
        

X=list(input().strip())
Y=list(input().strip())
table=[[-1 for _ in range(len(Y))]for _ in range(len(X))]

print(LCS(X,Y,len(X)-1,len(Y)-1,table))