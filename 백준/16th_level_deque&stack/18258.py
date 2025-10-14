import sys
input=sys.stdin.readline
from collections import deque

x=int(input())
arr=deque([])
print_list=[]
for i in range(0,x):
    y=input().split()
    if(y[0]=="push"):
        arr.append(y[1])
    elif(y[0]=="pop"):
        if(len(arr)==0):
            print_list.append(-1)
        else:
            print_list.append(arr[0])
            arr.popleft()
    elif(y[0]=="size"):
        print_list.append(len(arr))
    elif(y[0]=="empty"):
        if(len(arr)==0):
            print_list.append(1)
        else:
            print_list.append(0)
    elif(y[0]=="front"):
        if(len(arr)==0):
            print_list.append(-1)
        else:
            print_list.append(arr[0])

    elif(y[0]=="back"):
        if(len(arr)==0):
            print_list.append(-1)
        else:
            print_list.append(arr[-1])

for i in print_list:
    print(i)