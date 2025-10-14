x,y,z=map(int,input().split())

a=max(x,y,z)
b=a
if(a>=(x+y+z-a)):
    a=x+y+z-a-1

print(x+y+z-b+a)