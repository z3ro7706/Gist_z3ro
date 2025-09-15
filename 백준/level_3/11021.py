x=int(input())
list=[]
for i in range(0,x):
    a,b=map(int,input().split())
    list.append(a+b)
for i in range(0,x):
    print("Case #",i+1,": ", list[i],sep="")