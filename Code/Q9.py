import sys
input=sys.stdin.readline


def HappyNumbers(n):
    arr=list(str(n))
    if(n=='1'):
        return "true"
    if(len(arr)<=1):
        if(n==1):
            return "true"
        else:
            return "false"
    tot=0
    for i in arr:
        v=int(i)
        tot+=v*v
    return HappyNumbers(tot)
    
    
    
x=int(input())


print(HappyNumbers(x))
