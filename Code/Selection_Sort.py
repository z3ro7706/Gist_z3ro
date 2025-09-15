#해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘
#time complexity=O(n^2)

import sys
input=sys.stdin.readline

def Find_min_p(arr):
    min_p=0
    min=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]<=min):
            min_p=i
            min=arr[i]

    return min_p


def Selection(arr,p):
    if(len(arr)<=p):
        return arr
    
    key=int(Find_min_p(arr[p:]) + p)

    arr[p],arr[key]=arr[key],arr[p]

    return Selection(arr,p+1)

x=list(map(int,input().split()))
print(Selection(x,0))