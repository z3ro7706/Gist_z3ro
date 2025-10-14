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



n,m=map(int,input().split())
arr=list(map(int,input().split()))
if(len(arr)!=n):
    print("Wrong data list")
    exit(0)
b=[]

k=ascending(arr,b)
print(k[n-m])

