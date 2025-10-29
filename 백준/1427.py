import sys
input=sys.stdin.readline

def insertion(arr:list,x:int):
    if(x>=len(arr)):
        return arr
    for i in range(0,x):
        if(arr[i]<=arr[x]): #i 번째 위체에 현재 값을 넣어야함
            arr=arr[:i]+[arr[x]]+arr[i:x]+arr[x+1:]
    return insertion(arr,x+1)

def Sortinside(x:list):
    arr=insertion(x,0)
    return arr

    

a=list(map(int,input().strip()))
print(*Sortinside(a), sep='')