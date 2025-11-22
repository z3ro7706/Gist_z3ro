import sys
input = sys.stdin.readline

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


end_l = list(map(int, input().split()))
time_l = list(map(int, input().split()))
x=len(end_l)
if(x!=len(time_l)):
    print("Error")
    exit(0)


arr = []
for i in range(x):
    end = end_l[i]
    time = time_l[i]
    start = end - time
    arr.append([start, end, time])

arr = merge_sort(arr)

p = [-1] * x
for i in range(x):
    j = i - 1
    while j >= 0:
        if arr[j][1] <= arr[i][0]:
            p[i] = j
            break
        j -= 1
talbe = [0] * x



for i in range(x):
    val = arr[i][2]
    if p[i] != -1:
        val += talbe[p[i]]

    if i == 0:
        not_val = 0
    else:
        not_val = talbe[i - 1]
        
    if val > not_val:
        talbe[i] = val
    else:
        talbe[i] = not_val


print(talbe[x - 1])
