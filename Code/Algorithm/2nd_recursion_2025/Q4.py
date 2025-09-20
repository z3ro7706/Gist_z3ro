import sys
input=sys.stdin.readline

def StringPeriods(word:str,a:int,key:list):
    arr=list(word)

    if(a>=len(arr)):
        return key
    
    if(Judgment(arr,a) is True):
        return StringPeriods(arr,a+1,arr[:a])
    
    else:
        return StringPeriods(arr,a+1,key)


def Judgment(arr:list,length:int):
    if((len(arr)%length)!=0):
        return False
    
    for i in range(0,len(arr)):
        if(arr[i]!=arr[i%length]):
            return False
    return True

x=input().strip()
print(*StringPeriods(x,1,[-1]),sep="")