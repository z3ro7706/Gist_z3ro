import sys
input=sys.stdin.readline

arr=list(map(int, input().split(',')))

value_max=max(arr)
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
