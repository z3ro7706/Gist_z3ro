import sys
input=sys.stdin.readline

t,j=input()
arr=[]
for i in range(1,t+1):
    arr.append(i)

def Throwhankerchief(arr:list,n:int):
    if(len(arr)<=1):
        return arr[0]
    else:
        point=(n+j-1)%(len(arr))
        arr.remove(arr[point])
        n=point
        return Throwhankerchief(arr,n)


print(Throwhankerchief(arr,0))