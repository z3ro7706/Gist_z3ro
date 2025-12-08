import sys
input=sys.stdin.readline

def knapsack(n:int, m:int, p:list, w:list):
    if(n<=0 or m<=0):
        print("Data amount error")
        exit(0)

    if(len(p)!=n or len(w)!=n):
        print("List error")
        exit(0)

    Table=[[0]*(n+1) for _ in range (m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(j-w[i-1]<0):
                Table[i][j]=Table[i-1][j]
            else:
                Table[i][j]=max_t((Table[i-1][j]),(Table[i-1][(j-w[i-1])]+p[i-1]))
    return Table[-1][-1]


def max_t(x,y):
    if(x>=y):
        return x
    else:
        return y


print("Input data amount : ")
n=int(input().strip())
print("Input bag capacity : ")
m=int(input().strip())
print("Input data Price : ")
p=list(map(int,input().split()))
print("Input data weight : ")
w=list(map(int,input().split()))

print(knapsack(n,n,p,w))
