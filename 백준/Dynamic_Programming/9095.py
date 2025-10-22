import sys
input=sys.stdin.readline

def Combination(n):
    if(n<=1):
        return 1
    elif(n==2):
        return 2
    elif(n==3):
        return 4
    arr=[0]*n
    arr[0]=1
    arr[1]=2
    arr[2]=4

    for i in range(3,n):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]

    return arr[-1]

n=int(input())
for i in range(0,n):
    x=int(input())
    print(Combination(x))
