import sys
input=sys.stdin.readline

x=int(input().strip())
val=x%4

if(val==1 or val==3):
    print("SK")
else:
    print("CY")