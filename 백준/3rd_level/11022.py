a=int(input())
x=[]
y=[]
for i in range(0,a):
    n1,n2=map(int, input().split())
    x.append(n1)
    y.append(n2)
    
for i in range(0,a):
    print("Case #",i+1,": ",x[i]," + ",y[i]," = ", x[i]+y[i],sep="")