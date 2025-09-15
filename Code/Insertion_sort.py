#Time complexity = O(n^2)
#Using recurison

import sys
input=sys.stdin.readline

def Insertion(arr,p):
    if(len(arr)<=p):
        return arr

    for i in range(0,p):
        if(arr[i]>=arr[p]):
            arr=arr[:i]+[arr[p]]+arr[i:p]+arr[p+1:]
            
    return Insertion(arr,p+1)
    


x=list(map(int,input().split()))
print(Insertion(x,0))