def Find_min(a:list):
    min_=a[0]
    for i in a:
        if(i<min_):
            min_=i
    return min_

def ascending(a:list, b:list):
    c=Find_min(a)
    b.append(c)
    a.remove(c)
    if(len(a)==0):
        return b
    return ascending(a,b)

x=5 
n=[]
m=[]
for i in range(0,x):
    y=int(input())
    n.append(y)
k=ascending(n,m)
tot=0
for i in k:
    tot=tot+i
print(tot//len(k))
print(k[2])

