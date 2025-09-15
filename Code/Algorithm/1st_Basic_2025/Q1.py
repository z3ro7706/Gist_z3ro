import sys
input=sys.stdin.readline

n=int(input())

if(n<0 or n>18):
    print("Range error")
    exit(0)

    
value=1
for i in range(0,n):
    value=value*(i+1)

print(value)
