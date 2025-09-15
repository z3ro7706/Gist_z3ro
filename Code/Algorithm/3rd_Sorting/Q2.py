import sys
input=sys.stdin.readline

arr=list(map(int,input().split(',')))
count_list=[]

def find_max(arr):
    max=arr[0]
    for i in arr:
        if(i>=max):
            max=i
    return max

for i in range(0,len(arr)):
    key=arr[i]
    count=0
    for j in range(0,len(arr)):
        if(arr[j]==arr[i]):
            count+=1
    count_list.append(count)

if(find_max(count_list)>(len(arr)+1)//2):
    print("false")
else:
    print("true")

