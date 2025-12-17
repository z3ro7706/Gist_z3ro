import sys
input=sys.stdin.readline

def Insertion(arr:list,n:int):
    p=len(arr) #위치
    arr.append(n)

    while(Parent(p)>=0 and arr[p]>=arr[Parent(p)]):
        arr[p],arr[Parent(p)]=arr[Parent(p)],arr[p]
        p=Parent(p)

    return arr


def R_child(n:int):
    return 2*(n+1)

def L_child(n:int):
    return 2*n+1

def Parent(n:int):
    return (n-1)//2

arr=list(map(int,input().split(',')))
x=int(input())
print(Insertion(arr,x))