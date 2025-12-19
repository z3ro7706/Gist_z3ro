import sys
input=sys.stdin.readline

def Insertion(arr,p):
    arr.append(p)
    n=len(arr)-1
    while(P(n)>=0):
        if(arr[P(n)]<=arr[n]):
            arr[P(n)],arr[n]=arr[n],arr[P(n)]
            n=P(n)
        else:
            break
    return arr

def R(n):
    return 2*n+1

def L(n):
    return 2*(n+1)

def P(n):
    return (n-1)//2

x=list(map(int,input().split(',')))
n=int(input())
print(Insertion(x,n))