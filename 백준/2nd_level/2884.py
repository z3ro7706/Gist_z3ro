h,m=map(int, input().split())
if(0<=h<=23 and 0 <= m <= 59):
  if(m>=45):
    m=m-45
    print(h,m)
  else:
    if(h==0):
        h=23
    else:
        h=h-1
    m=m+15
    print(h , m)
else:
    exit(1)