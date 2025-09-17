import sys
input=sys.stdin.readline


arr=list(map(int,input().split(',')))


def combine(a,b):
    arr=[]
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


arr_sort=merge_sort(arr)

print(arr_sort[1],arr_sort[-2])
