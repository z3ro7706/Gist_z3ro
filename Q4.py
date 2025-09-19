import sys
input=sys.stdin.readline

def StringPeriods(word:str,a:int,key):
    arr=list(word)

    if(len(arr)<=1):
        return -1
        
    if(len(arr)//2<a):
        return key
    
    if(len(arr)%a!=0):
        return StringPeriods(arr,a+1,key)
    key_n=[]
    for i in range(0,a):
        key_n.append(arr[i])

    for i in range(0,len(arr)):
        if(arr[i]!=key_n[i%a]):
            return StringPeriods(arr,a+1,key_n)

    return StringPeriods(arr,a+1,key_n)


x=input().strip()
print(*StringPeriods(x,1,-1),sep="")