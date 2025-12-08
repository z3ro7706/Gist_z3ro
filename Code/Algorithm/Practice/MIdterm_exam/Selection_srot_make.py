import sys
input=sys.stdin.readline


def Selection_sort(arr,pivot):
    if(pivot>=len(arr)-1):
        return arr
    
    key=Find_min_position(arr[pivot:])+pivot
    arr[pivot],arr[key] =arr[key],arr[pivot]

    return Selection_sort(arr,pivot+1)


def Find_min_position(arr):
    min=arr[0]
    key=0
    for i in range(0,len(arr)):
        if(arr[i]<=min):
            key=i
            min=arr[i]

    return key


arr=list(map(int,input().split()))
print(Selection_sort(arr,0))

