import sys
input= sys.stdin.readline

n=int(input())
if(n<1):
    print("value_error")
    exit(0)
elif(n==1):
    print(0)
    exit(0)

arr=[0]*n

arr[1]=1
for i in range(2,n):
    if((i+1)%2==0 and (i+1)%3==0): #둘다 나눠진다면
        arr[i]=min(arr[(i-1)//2]+1,arr[(i-2)//3]+1,arr[i-1]+1)
    elif((i+1)%2==0 and (i+1)%3!=0): #2로 나눠진다면
        arr[i]=min(arr[(i-1)//2]+1,arr[i-1]+1)
    elif((i+1)%2!=0 and (i+1)%3==0): #3로 나눠진다면
        arr[i]=min(arr[(i-2)//3]+1,arr[i-1]+1)
    else:
        arr[i]=arr[i-1]+1

print(arr[-1])