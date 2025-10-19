import sys
input=sys.stdin.readline

arr=list(map(int, input().split(',')))

def ArrayAdditionI(arr):
    max=arr[0]
    for i in arr:
        if(i>=max):
            max=i
    return max

value_max=ArrayAdditionI(arr)
arr.remove(value_max)

add_list = set()
l = len(arr)

def add(t,c):
    if c < l:
        add(t+arr[c],c+1)
        add(t,c+1)
    else:
        add_list.add(t)

add(0,0)
if(value_max in add_list):
    print("true")
else:
    print("false")
