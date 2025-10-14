for i in range(0,10000):
    x,y=map(int,input().split())
    if(x==0 and y==0):
        exit(0)

    if(x%y==0):
        print("multiple")
    elif(y%x==0):
        print("factor")
    else:
        print("neither")
