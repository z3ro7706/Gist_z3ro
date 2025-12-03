import sys
input = sys.stdin.readline

def Bonusbudget(arr1:list) -> int:
    n=len(arr1)
    if (n==0):
        return 0
    
    arr2=[1]*n
    i = 1

    while (i<n):
        if(arr1[i]>arr1[i-1] and arr2[i]<=arr2[i-1]):
            arr2[i]=arr2[i-1]+1
        i+=1

    i = n - 2
    while i>= 0:
        if (arr1[i]>arr1[i+1] and arr2[i]<=arr2[i+1]):
            arr2[i]=arr2[i+1]+1
        i-=1

    total=0
    for v in arr2:
        total+=v

    return total*1000


arr=list(map(int,input().split(',')))
print(Bonusbudget(arr))
