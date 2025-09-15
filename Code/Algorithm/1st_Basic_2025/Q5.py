import sys
input=sys.stdin.readline

arr=list(input())
arr_new=[]

key=arr[0]
count=0
for i in range(0,len(arr)):
    if(arr[i]==key):
        count+=1
    else:
        arr_new.append(count)
        arr_new.append(key)
        key=arr[i]
        count=1

print(*arr_new,sep="")