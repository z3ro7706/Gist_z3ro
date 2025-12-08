import sys
input=sys.stdin.readline

def merge_sort(arr:list):
    if(len(arr)<=1):
        return arr
    length=len(arr)
    mid=length//2
    return combine(merge_sort(arr[:mid]),merge_sort(arr[mid:]))

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

un=list(map(int,input().split()))
print(*merge_sort(un))
