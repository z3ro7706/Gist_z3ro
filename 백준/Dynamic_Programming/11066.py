import sys
input=sys.stdin.readline


def Zip_fill(x:list):
    if(len(x)<=1):
        return arr[0]+arr[1]
    
    min=sys.maxsize
    cost=0
    for k in range(1,len(x)):
        cost=Zip_fill(x[:k])+Zip_fill(x[k:])+x[k]+x[k+1]
        if(cost<=min):
            min=cost

    return cost

x=int(input())
for i in range(0,x):
    y=int(input())
    arr=list(map(int,input().split()))
    if(len(arr)!=y):
        print("Input error")
        exit(0)
    print(Zip_fill(arr))


