import sys
input=sys.stdin.readline

def LCS_W(X:list,Y:list,n:int,m:int,table:list):
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1]==Y[j-1]):
                table[i][j]=table[i-1][j-1]+1
            else:
                table[i][j]=_max(table[i-1][j],table[i][j-1]) #table 완성

    x=n
    y=m
    arr=[]
    while(table[x][y]>0):
        if(table[x][y]==table[x-1][y]):
            x-=1
        elif(table[x][y]==table[x][y-1]):
            y-=1
        else:
            arr.append(X[x-1])
            x-=1
            y-=1
    return reversed(arr)
            
    



def _max(x,y):
    if(x>=y):
        return x
    else:
        return y

x=list(input().strip())
y=list(input().strip())

table=[[0 for _ in range(len(y)+1)]for _ in range(len(x)+1)]

print(*LCS_W(x,y,len(x),len(y),table), sep='')