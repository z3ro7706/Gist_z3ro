arr=[]
for i in range(0,10):
    x=int(input())
    if(x<0 or x>1000):
        exit(0)
    y=x%42
    cal=0
    for i in arr:
        if(i==y):
            cal = 1
        else:
            pass
        
    if(cal==1):
        pass
    else:
        arr.append(y)

print(len(arr))