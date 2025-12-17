import sys
input=sys.stdin.readline

def LCS(X:list,Y:list,i:int,j:int):
    if(i<=0 or j<=0):
        return 0
    else:
        if(X[i-1]==Y[j-1]):
            return LCS(X,Y,i-1,j-1)+1
        else:
            return _max(LCS(X,Y,i-1,j),LCS(X,Y,i,j-1))
        

        
def _max(x,y):
    if(x>=y):
        return x
    else: 
        return y

x=list(input().strip())
y=list(input().strip())
print(LCS(x,y,len(x),len(y)))