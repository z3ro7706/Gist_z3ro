import sys
input=sys.stdin.readline


def heap_Sort(arr:list,p:int):
    if(p<=0):
        return arr
    if(p==1):
        if(arr[0]>arr[1]):
            arr[0],arr[1]=arr[1],arr[0]
        return arr
    else:
        arr[0],arr[p]=arr[p],arr[0]
        return heap_Sort(heapify(arr[:p],0,0) + arr[p:],p-1)



def heapify(arr:list,p:int,c:int):
    if(p<0):
        return arr
    
    if(L_child(c)>=len(arr)): #자식노드가 없는경우

        return heapify(arr,p-1,p-1)
    
    else: #자식노드가 있는 경우
        if(R_child(c)>=len(arr)): #오른쪽 노드가 없다면
            if(arr[L_child(c)]>=arr[c]):
                arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                return heapify(arr,p,L_child(c))
            else:
                return heapify(arr,p-1,p-1)
        else: #모든 child node가 존재하는 경우
            if(arr[R_child(c)]>=arr[c] or arr[L_child(c)]>=arr[c]):
                if(arr[R_child(c)]>=arr[L_child(c)]):
                    arr[R_child(c)],arr[c]=arr[c],arr[R_child(c)]

                    return heapify(arr,p,R_child(c))
                else:
                    arr[L_child(c)],arr[c]=arr[c],arr[L_child(c)]
                    return heapify(arr,p,L_child(c))
            else:
                return heapify(arr,p-1,p-1)

def L_child(n:int):
    return(2*n+1)

def R_child(n:int):
    return(2*(n+1))

def Perent(n:int):
    return (n-1)//2

arr=list(map(int,input().split()))
arr_n=heapify(arr,len(arr)-1,len(arr)-1)
print(arr_n)

print(heap_Sort(arr_n,len(arr_n)-1))