x=int(input()) #거슬러줘야 할 case

for i in range(0,x):
    cost=int(input())
    if(cost<0 or cost>500):
        exit(0)

    arr=[]
    Quarter=cost//25
    cost=cost-25*Quarter
    Dime=cost//10
    cost=cost-10*Dime
    Nickel=cost//5
    cost=cost-5*Nickel
    Penny=cost
    arr.append(Quarter)
    arr.append(Dime)
    arr.append(Nickel)
    arr.append(Penny)
    print(*arr)

