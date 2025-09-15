import sys
input=sys.stdin.readline

def NumberReverse(s):
    return s[::-1]

arr=list(input().split())
print(*NumberReverse(arr))