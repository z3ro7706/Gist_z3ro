import sys
input = sys.stdin.readline
count_r=1
count_d=1
def fibonacci_r(n):
    global count_r
    if(n==1 or n==2):
        return 1
    else:
        count_r+=1
        return(fibonacci_r(n-1)+fibonacci_r(n-2))
    

def fibonacci_d(n):
    global count_d
    if n<=1:
        
        return n

    arr=[0]*(n+1)
    arr[1]=1

    for i in range(2,n+1):
        count_d+=1
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

import sys
input=sys.stdin.readline

n=int(input())
fibonacci_r(n)
fibonacci_d(n)


print(count_r,count_d-2)
