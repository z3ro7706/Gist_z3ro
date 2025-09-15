import sys
input=sys.stdin.readline

def FirstFacorial(n):
    if(n<=1):
        return 1
    
    num=FirstFacorial(n-1)*n
    return num

x=int(input())
print(FirstFacorial(x))

