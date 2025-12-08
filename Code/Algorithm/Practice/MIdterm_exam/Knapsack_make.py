import sys
input= sys.stdin.readline

def Knapsack(n:int, m:int, p:list, w:list):

    if(n<=0 or m<=0):
        print("Data Amount Error or Capacity Error ")

    if(len(p)!=n):
        print("Price list error")
        exit(0)

    if(len(w)!=n):
        print("Weight list error")
        exit(0)

    Table=[[0]*(n+1)]*(m+1)

    for i in range(1,n+1):
        for j in range(1,m+1):
            Table[i,j]=max_t(Table[i-1,j],Table(i-1,j-w[i])+p[i])
    
    return Table[-1][-1]

def max_t(a,b):
    if(a>=b):
        return a
    else:
        return b

#data input
print("Input data amount : ")
n=int(input())
print("Input bag capacity : ")
m=int(input())
print("Input data Price : ")
p=list(map(int,input().split()))
print("Input data weight : ")
w=list(map(int,input().split()))

print(Knapsack(n,n,p,w))


