import sys
input=sys.stdin.readline

def  value_down(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    
    if a>=20 or b>=20 or c>=20:
        return 10485786
    
    if(a<b and b<c):
        return value_down(a,b,c-1)+value_down(a,b-1,c-1)-value_down(a,b-1,c)
    else:
        return value_down(a-1,b,c)+value_down(a-1,b-1,c)+value_down(a-1,b,c-1)-value_down(a-1,b-1,c-1)
    

while(1):
    a,b,c=map(int,input().split())
    if(a==-1 and b==-1 and c==-1):
        break
    d=a
    e=b
    f=c
    if(a>20 or b>20 or c>20):
        a=20
        b=20
        c=20
    print("W(",d,", ",e,", ",f,") = ",value_down(a,b,c),sep="")