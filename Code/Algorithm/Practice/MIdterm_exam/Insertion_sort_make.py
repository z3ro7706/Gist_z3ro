import sys
input=sys.stdin.readline

def Insertion_sort(arr,pivot):
    if(pivot>=len(arr)):
        return arr
    
    for i in range(0,pivot):
        if(arr[i]>=arr[pivot]):
            arr=arr[0:i]+[arr[pivot]]+arr[i:pivot]+arr[pivot+1:]

    return Insertion_sort(arr,pivot+1)


arr=list(map(int,input().split()))
print(Insertion_sort(arr,0))