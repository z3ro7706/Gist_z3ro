import sys
input=sys.stdin.readline

def Delete(arr:list):
    n=len(arr)-1
    p=0
    arr[0],arr[n]=arr[n],arr[0]
    arr.pop()
    while(L_child(p)<n): #자식 노드가 존재한다면
        if(R_child(p)<n): # 자식 노드가 둘다 존재한다면
            if(arr[p]<=arr[R_child(p)] or arr[p]<=arr[L_child(p)]):
                if(arr[R_child(p)]>=arr[L_child(p)]):
                    arr[p],arr[R_child(p)]=arr[R_child(p)],arr[p]
                    p=R_child(p)
                else:
                    arr[p],arr[L_child(p)]=arr[L_child(p)],arr[p]
                    p=L_child(p)
            else:
                break
        else:
            if(arr[p]<=arr[L_child(p)]): 
                arr[p],arr[L_child(p)]=arr[L_child(p)],arr[p]
                p=L_child(p)
            else:
                break
    return arr



def _max(x,y):
    if(x>=y):
        return x
    else:
        return y
    
def R_child(n:int):
    return 2*(n+1)

def L_child(n:int):
    return 2*n+1

def Parent(n:int):
    return (n-1)//2

x=list(map(int,input().split(',')))
print(Delete(x))