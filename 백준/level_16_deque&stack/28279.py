import sys
input=sys.stdin.readline
from collections import deque

x=int(input())

arr=deque([])

def operator2(a:int, b:int):
    if(a==1):
        arr.appendleft(b)
    elif(a==2):
        arr.append(b)
    else:
        print("operator error")

def operator1(a:int):
    if(a==3):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr.popleft())
    elif(a==4):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr.pop())
    elif(a==5):
        print(len(arr))
    elif(a==6):
        if(len(arr)==0):
            print(1)
        else:
            print(0)
    elif(a==7):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr[0])

    elif(a==8):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr[-1])
    else:
        print("first input value error")


for i in range(0,x):
    y=list(input().split())
    if(len(y)==1):
        operator1(int(y[0]))
    elif(len(y)==2):
        operator2(int(y[0]),int(y[1]))
    else:
        print("input error")
    
