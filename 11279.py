#시관초과 해결필요(heap구조  -> tree 형태로 나아가서 시간을 줄이자)

import sys
input=sys.stdin.readline

def heap_0(arr:list):
    if(len(arr)<=0):
        print(0)
        return arr
    else:
        print(arr[-1])
        arr.pop()
        return arr
    
def heap_other(arr:list,n:int):
     if(len(arr)<=0):
         arr.append(n)
         return arr
     
     if(arr[0]>=n):
            return [n]+arr
        
     if(arr[-1]<=n):
        return arr+[n]
     
     for i in range(0,len(arr)-1):
        if(arr[i]<=n<=arr[i+1]):
            return arr[:i]+[n]+arr[i:]

     print("Error")
     exit(0)

n=int(input().strip())
arr=[]
for i in range(0,n):
    x=int(input())
    if(x==0):
        arr=heap_0(arr)
    else:
        arr=heap_other(arr,x)