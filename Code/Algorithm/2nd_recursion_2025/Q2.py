import sys
input=sys.stdin.readline

arr=list(map(int,input().split(',')))
arr_sort=[]

def find_min(arr):
    min=arr[0]
    for i in arr:
        if(i<min):
            min=i
    return min


def SortArrayusingrecursion(arr:list,arr_sort:list):
    if(len(arr)<=0):
        return arr_sort
    
    else:
        x=find_min(arr)
        arr.remove(x)
        arr_sort.append(x)
        return SortArrayusingrecursion(arr,arr_sort)

print(SortArrayusingrecursion(arr,arr_sort))