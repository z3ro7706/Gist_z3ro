import sys
input=sys.stdin.readline

def LCS(X,Y,i,j,m):
    if(i<=0 or j<=0):
        return 0
    
    if(m[i][j]!=-1):
        return m[i][j]
    else:
        if(X[i-1]==Y[j-1]):
            m[i][j]= LCS(X,Y,i-1,j-1,m)+1
            return m[i][j]
        else:
            m[i][j]= _max(LCS(X,Y,i-1,j,m),LCS(X,Y,i,j-1,m))
            return m[i][j]
        


def _max(x,y):
    if(x>=y):
        return x
    else:
        return y


X=list(input())
Y=list(input())

m = [[-1 for _ in range(len(Y))]for _ in range(len(X))]

print(LCS(X,Y,len(X)-1,len(Y)-1,m))