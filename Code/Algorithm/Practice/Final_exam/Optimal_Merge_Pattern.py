import sys
input=sys.stdin.readline

def Optimal_Merge_pattern(arr:list,t:int):
    if(len(arr)<=1):
        return t + arr[0]
    
    if(len(arr)==2):
        return arr[0]+arr[1] + t
    
    c=0
    for i in range(0,2):
        c+=arr[0]
        arr=Delete(arr)

    arr=Insertion(arr,c)

    return Optimal_Merge_pattern(arr,t+c)

def Insertion(arr:list,n:int):
    p=len(arr) #위치
    arr.append(n)

    while(Parent(p)>=0 and arr[p]<=arr[Parent(p)]):
        arr[p],arr[Parent(p)]=arr[Parent(p)],arr[p]
        p=Parent(p)

    return arr


def Heapify(arr:list):
    n=p=len(arr)-1
    
    while(p>=0): # p : 처음 탐색 위치, c : 현재 탐색 위치
        c=p
        while(L_child(c)<=n): #자식 노드가 존재할때 까지 반복
            if(R_child(c)<=n): #자식 노드가 모두 존재한다면
                if(arr[R_child(c)]<=arr[c] or arr[L_child(c)]<=arr[c]):
                    if(arr[R_child(c)]<=arr[L_child(c)]):
                        arr[R_child(c)],arr[c]=arr[c],arr[R_child(c)]
                        c=R_child(c)
                    else:
                        arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                        c=L_child(c)
                else:
                    break
            else:
                if(arr[L_child(c)]<=arr[c]):
                    arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                    c=L_child(c)
                else:
                    break
        p-=1

    return arr

def Delete(arr:list):
    n=len(arr)-1
    p=0
    arr[0],arr[n]=arr[n],arr[0]
    arr.pop()
    while(L_child(p)<n): #자식 노드가 존재한다면
        if(R_child(p)<n): # 자식 노드가 둘다 존재한다면
            if(arr[p]>=arr[R_child(p)] or arr[p]>=arr[L_child(p)]):
                if(arr[R_child(p)]<=arr[L_child(p)]):
                    arr[p],arr[R_child(p)]=arr[R_child(p)],arr[p]
                    p=R_child(p)
                else:
                    arr[p],arr[L_child(p)]=arr[L_child(p)],arr[p]
                    p=L_child(p)
            else:
                break
        else:
            if(arr[p]>=arr[L_child(p)]): 
                arr[p],arr[L_child(p)]=arr[L_child(p)],arr[p]
                p=L_child(p)
            else:
                break
    return arr


def R_child(n:int):
    return 2*(n+1)

def L_child(n:int):
    return 2*n+1

def Parent(n:int):
    return (n-1)//2

arr=list(map(int,input().split()))

print(Optimal_Merge_pattern(Heapify(arr),0))