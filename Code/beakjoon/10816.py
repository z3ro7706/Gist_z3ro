import sys
input=sys.stdin.readline

#merge sort
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


#binary_serach
def binary_search(arr, key,count):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            count+=1
            break
        elif arr[mid] < key:
            left = mid + 1      # 오른쪽 구간으로 이동
        else:
            right = mid - 1     # 왼쪽 구간으로 이동
    mid_r=mid
    mid_l=mid
    while(arr[mid_r]==key):
        count+=1
        mid_r+=1
        if(mid_r>=len(arr)):
            break

    while(arr[mid_l]==key):
        count+=1
        mid_l-=1
        if(mid_l<0):
            break

    if(count!=0):
        count=count-2
    return count

#value input
v_target=int(input())
target=list(map(int,input().split()))
if(len(target)!=v_target):
    print("Target error")
    exit(0)

v_find=int(input())
find=list(map(int,input().split()))

if(len(find)!=v_find):
    print("Find error")
    exit(0)
arr_new = merge_sort(target)
for i in find:
    count=0
    print(binary_search(arr_new,i,count))


