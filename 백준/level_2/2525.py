h,m = map(int, input().split())
x=int(input())
m=m+x
if(0<=m<60):
    pass
else:
    while(m>=60):
        h=h+1
        m=m-60
        if(h==24):
            h=0
print(h,m)


 