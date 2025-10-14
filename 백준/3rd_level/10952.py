x=[]
y=[]

while True:
    n1,n2=map(int, input().split())
    if(n1==0 and n2==0):
        break
    x.append(n1)
    y.append(n2)
    
for i in range(0,len(x)):
    print(x[i]+y[i])
    