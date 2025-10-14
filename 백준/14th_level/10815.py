"""
def check_reduplication(arr):
    new_arr=[]
    for i in arr:
        count=0
        for j in new_arr:
            if(j==i):
                count+=1
        if(count==0):
            new_arr.append(i)
    return new_arr
"""

def Find_max(arr):
    max=arr[0]
    for i in arr:
        if(i>max):
            max=i
    return max

#Counting_sort
def counting_sort(arr): #매핑으로 음수 해결
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count_arr = [0] * range_val

    # 카운팅
    for num in arr:
        count_arr[num - min_val] += 1

    # 누적합
    for i in range(1, range_val):
        count_arr[i] += count_arr[i - 1]

    output_arr = [0] * len(arr)

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] - min_val
        output_arr[count_arr[index] - 1] = arr[i]
        count_arr[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]



#Binary_search
def binary_search(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return False



#input_Data
n=int(input())
Have_list=list(map(int, input().split()))
m=int(input())
Find_list=list(map(int, input().split()))

#DEBUGIN
if(n!=len(Have_list) or m!=len(Find_list)): #잘못된 양의 데이터를 받음
    print("Wrong Data")
    exit(0)

if(m<0 or m>500000 or n<0 or n>500000): #잘못된 양의 데이터를 받음
    print("Wrong Card amount")
    exit(0)

for i in Have_list: #잘못된 데이터 범위
    if(i>10000000 or i<-10000000):
        print("Wrong input list value")

for i in Find_list: #잘못된 데이터 범위
    if(i>10000000 or i<-10000000): 
        print("Wrong Find list value")

"""
if(n!=len(check_reduplication(Have_list))):
   print("Have a reduplicaition of have list")
   exit(0)

if(m!=len(check_reduplication(Find_list))):
   print("Have a reduplicaition of Find list")
   exit(0)
"""

counting_sort(Have_list) #Have_list가 정렬됨
print_value=[]
for i in range(0,len(Find_list)):
    Check=binary_search(Have_list,Find_list[i])
    if(Check==True):
        print_value.append(1)
    else:
        print_value.append(0)

print(*print_value)