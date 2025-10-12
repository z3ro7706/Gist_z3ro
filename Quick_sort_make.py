import sys
input=sys.stdin.readline

def Quick_sort(arr):
    if(len(arr)<=1):
        return arr
    
    arr_l=[]
    arr_r=[]
    pivot=arr[0]

    for i in range(1,len(arr)):
        if(arr[i]<=pivot):
            arr_l.append(arr[i])
        else:
            arr_r.append(arr[i])

        arr_n=Quick_sort(arr_l)+[pivot]+Quick_sort(arr_r)

    return arr_n


arr=list(map(int,input().split()))
print(*Quick_sort(arr))