import sys
input=sys.stdin.readline

def Heapify(arr:list):
    n=p=len(arr)-1
    
    while(p>=0): # p : 처음 탐색 위치, c : 현재 탐색 위치
        c=p
        while(L_child(c)<=n): #자식 노드가 존재할때 까지 반복
            if(R_child(c)<=n): #자식 노드가 모두 존재한다면
                if(arr[R_child(c)]>=arr[c] or arr[L_child(c)]>=arr[c]):
                    if(arr[R_child(c)]>=arr[L_child(c)]):
                        arr[R_child(c)],arr[c]=arr[c],arr[R_child(c)]
                        c=R_child(c)
                    else:
                        arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                        c=L_child(c)
                else:
                    break
            else:
                if(arr[L_child(c)]>=arr[c]):
                    arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                    c=L_child(c)
                else:
                    break
        p-=1

    return arr


def R_child(n:int):
    return 2*(n+1)

def L_child(n:int):
    return 2*n+1

def Parent(n:int):
    return (n-1)//2

arr=list(map(int,input().split(',')))
print(Heapify(arr))