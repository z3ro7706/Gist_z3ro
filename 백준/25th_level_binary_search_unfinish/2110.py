import sys
input=sys.stdin.readline

n,c=map(int,input().split())


def combine(a,b):
    arr=[] #합쳐진 새로운 sort정렬
    point_1=0
    point_2=0
    for i in range(len(a)+len(b)):
        if(len(a)<=point_1):
            while(len(b)>point_2):
                arr.append(b[point_2])
                point_2+=1
            break

        if(len(b)<=point_2):
            while(len(a)>point_1):
                arr.append(a[point_1])
                point_1+=1
            break

         #작은 수만 집어 넙기       
        if(a[point_1]>=b[point_2]):
            arr.append(b[point_2])
            point_2+=1

        elif(a[point_1]<b[point_2]):
            arr.append(a[point_1])
            point_1+=1

    return arr

def merge_sort(a):
    if(len(a)<=1):
        return a
    mid=len(a)//2
    return combine(merge_sort(a[:mid]),merge_sort(a[mid:]))

def add(arr: list):
    if len(arr) < 2:
        return arr

    arr_n = []
    for i in range(0, len(arr) - 1):
        arr_n.append(arr[i] + arr[i + 1])

    key = arr_n[0]
    key_v = 0
    for i in range(1, len(arr_n)):
        if arr_n[i] < key:
            key = arr_n[i]
            key_v = i

    s = arr[key_v] + arr[key_v + 1]
    arr[key_v] = s
    del arr[key_v + 1]

    return arr

arr=[]
arr_new=[]
arr_gap=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)

arr_new=merge_sort(arr)

for i in range(0,n-1):
    arr_gap.append(arr_new[i+1]-arr_new[i])  #건물 사이의 거리를 리스트에 넣음

while(1):
    if(len(arr_gap)<c):
        print(min(arr_gap))
        exit(0)
    add(arr_gap)

