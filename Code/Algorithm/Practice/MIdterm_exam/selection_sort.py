import sys
input=sys.stdin.readline

def selection(arr:list,x:int):
    if(x>=len(arr)):
        return arr
    min=arr[x]
    min_p=x
    for i in range(x,len(arr)):
        if(arr[i]<=min):
            min=arr[i]
            min_p=i

    if(min_p!=x):
        arr[x],arr[min_p]=arr[min_p],arr[x]
    
    return selection(arr,x+1)
    
un=list(map(int,input().split()))
print(*selection(un,0))