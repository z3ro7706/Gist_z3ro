x=int(input())

value=list(map(int,input().split()))

if(len(value)!=x):
    print("input error")

if(x==1):
    print(value[0]*value[0])
else:
    print(max(value)*min(value))