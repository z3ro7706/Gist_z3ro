import sys
input=sys.stdin.readline

def FirstReverse(str):
    return str[::-1]



arr=list(input().strip())
print(*FirstReverse(arr),sep="")