n1,n2=map(int,input().split())

if(n1<0 or n1>=1000 or n2<0 or n2>=1000):
    exit(0)

for i in range(0,3):
    a=n1//100
    b=(n1-a*100)//10
    c=n1-100*a-b*10
    n1=100*c+10*b+a

for i in range(0,3):
    a=n2//100
    b=(n2-a*100)//10
    c=n2-100*a-b*10
    n2=100*c+10*b+a

if n1>n2:
    print(n1)
else:
    print(n2)