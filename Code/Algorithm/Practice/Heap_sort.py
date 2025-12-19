import sys
input=sys.stdin.readline


def Heapify(arr):
    k=len(arr)-1
    p=len(arr)-1
    while(p>=0):
        n=p
        while(L(n)<=k):
            if(R(n)<=k):
                if(arr[L(n)]>=arr[n] or arr[R(n)] >= arr[n]):
                    if(arr[L(n)]>=arr[R(n)]):
                        arr[L(n)],arr[n]=arr[n],arr[L(n)]
                        n=L(n)
                    else:
                        arr[R(n)],arr[n]=arr[n],arr[R(n)]
                        n=R(n)
                else:
                    break
            else:
                if(arr[L(n)]>=arr[n]):
                    arr[L(n)],arr[n]=arr[n],arr[L(n)]
                    n=L(n)
                else:
                    break
        p-=1
    return arr

def R(n):
    return 2*n+1

def L(n):
    return 2*(n+1)

def P(n):
    return (n-1)//2

arr=list(map(int,input().split(',')))
print(Heapify(arr))