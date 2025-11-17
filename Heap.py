import sys
input=sys.stdin.readline

def Make_heap(arr:list):
    if(len(arr)<=1):
        return arr
    arr_heap=[]
    arr_heap.append(arr[0])
    for i in range(1,len(arr)):
            arr_heap=Heap_append(arr_heap,arr[i])

    return arr_heap
        

def Heap_append(arr:list,n:int):
    if(len(arr)<1):
        return arr
    
    arr.append(n) # heap 정렬이 되지 않은 arr
    length=len(arr) 
    point=length-1
    parent=(point-1)//2
    while(point>=0 and parent>=0 and arr[point]>=arr[parent]): #현재 위치가 arr 안에 존재 + arr의 parent 가 존재 + 현재 위치의 값이 parent보다 클떄 진행
        arr[point],arr[parent]=arr[parent],arr[point] #둘을 스윕
        point=parent #현재 위치를 바뀐 위치로 바꾸기
        parent=(point-1)//2 #새로운 paraent point 잡아주기

    return arr

def Delete_max_heap(arr:list):
    arr[0],arr[-1]=arr[-1],arr[0] #max와 맨 아래 값을 서로 swqp
    print(arr[-1])
    arr.remove(arr[-1]) #마지막 리스트 제거 (max 값 제거)
    if(len(arr)<=3):
        arr=Make_heap(arr)
        return arr
    
    point=0
    child_l=(point*2)+1
    child_r=(point*2)+2

    if(arr[child_l]>=arr[child_r]):
        child=child_l
    else:
        child=child_r

    while(point<len(arr)and child<len(arr) and arr[child]>=arr[point]):
        arr[point],arr[child]=arr[child],arr[point]

        point=child
        child_l=(point*2)+1
        child_r=(point*2)+2
        if(child_l>=len(arr)):
            child=len(arr)+1
        elif(child_r>=len(arr)):
            child=child_l
        elif(arr[child_l]>=arr[child_r]):
            child=child_l
        else:
            child=child_r
    return arr
    

def Find_max(arr):
    max=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]>=max):
            max=arr[i]
    return max

def Find_max_point(arr):
    max=arr[0]
    max_p=0
    for i in range(0,len(arr)):
        if(arr[i]>=max):
            max=arr[i]
            max_p=i
    return max_p

arr=list(map(int,input().split()))
arr=Make_heap(arr)
print(Delete_max_heap(arr))

    