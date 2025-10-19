for i in range(0,100000):
    x=int(input())
    if(x==-1):
        exit(0)
    arr=[]
    for i in range(1,x):
        if(x%i==0):
            arr.append(i)
    val=0
    for i in arr:
        val=val+i
    if(val!=x):
        print(x, "is NOT perfect.")
    else:
        print(x,"= ",end="")
        print(' + '.join(map(str, arr)))





