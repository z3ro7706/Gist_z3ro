import sys
input=sys.stdin.readline

def SimpleAdding(n):
    if(n<=1):
        return 1
    return SimpleAdding(n-1)+n

x=int(input())
print(SimpleAdding(x))

