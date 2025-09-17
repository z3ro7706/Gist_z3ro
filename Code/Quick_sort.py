#pivot을 잡고, 이를 기준으로 크기를 비교하여 위치 나눔
# Time Complexity = O(n log n) , 최악의 경우 한쪽으로 쏠림이 발생해 O(n^2)까지 증가
# Space Complexity = O(log n )-> 별도의 공간을 필요로 하지 않음

import sys
input = sys.stdin.readline

def Quick_sort(arr):
    if(len(arr)<=1):
        return arr
    
    pivot=arr[0]
    arr_l=[]
    arr_r=[]

    for i in range(1,len(arr)):
        if(arr[i]<=pivot):
            arr_l.append(arr[i])
        else: #(arr[i]>pivot):
            arr_r.append(arr[i])

    arr_n=Quick_sort(arr_l)+[pivot]+Quick_sort(arr_r)
    return arr_n
    
x=list(map(int,input().split()))
print(Quick_sort(x))