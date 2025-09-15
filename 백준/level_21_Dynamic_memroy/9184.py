import sys
input=sys.stdin.readline


data_base=[[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)]


def  value_down(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    
    if a>20 or b>20 or c>20:
        return value_down(20,20,20)
    
    if data_base[a][b][c] != 0:
        return data_base[a][b][c]
    
    if(a<b and b<c):
        data_base[a][b][c]=value_down(a,b,c-1)+value_down(a,b-1,c-1)-value_down(a,b-1,c)
        return data_base[a][b][c]

    else:
        data_base[a][b][c]=value_down(a-1,b,c)+value_down(a-1,b-1,c)+value_down(a-1,b,c-1)-value_down(a-1,b-1,c-1)
        return data_base[a][b][c]

while(1):
    a,b,c=map(int,input().split())
    if(a==-1 and b==-1 and c==-1):
        break
    d=a
    e=b
    f=c
    print("w(",d,", ",e,", ",f,") = ",value_down(a,b,c),sep="")