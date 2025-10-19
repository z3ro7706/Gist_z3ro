import sys
input=sys.stdin.readline

def Compression(arr:list,n):
    if(len(arr)<2*n):
        return arr
    
    for i in range(0,len(arr)-2*n+1):
        if(arr[i:i+n]==arr[i+n:i+2*n]):
            arr=arr[:i+n]+arr[i+2*n:]
            return Compression(arr,n)
    
    return Compression(arr,n+1)


x=list(input().strip())
print(*Compression(x,1), sep='')
    