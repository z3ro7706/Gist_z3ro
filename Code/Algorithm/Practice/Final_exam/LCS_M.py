import sys
input=sys.stdin.readline

def LCS(X:list,Y:list,i:int,j:int,table:list):
    if(i<=0 or j<=0):
        return 0
    
    if(table[i][j]!=-1):
        return table[i][j]
    else:
        if(X[i-1]==Y[j-1]):
            table[i][j]=LCS(X,Y,i-1,j-1,table)+1
            return table[i][j]
        else:
            table[i][j]=_max(LCS(X,Y,i-1,j,table),LCS(X,Y,i,j-1,table))
            return table[i][j]
        
def _max(x,y):
    if(x>=y):
        return x
    else:
        return y
    
x=list(input().strip())
y=list(input().strip())
table=[[-1 for _ in range(len(y)+1)]for _ in range(len(x)+1)]

print(LCS(x,y,len(x),len(y),table))