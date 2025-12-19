import sys
input=sys.stdin.readline

def R(n):
    return 2*n+1

def L(n):
    return 2*(n+1)

def P(n):
    return (n-1)//2

def Delete(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    v=arr.pop()
    print(v)
    n=0
    p=len(arr)-1
    while(L(n)<=p):
        if(R(n)<=p):
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
    
    return arr

arr=list(map(int,input().split(',')))
print(Delete(arr))