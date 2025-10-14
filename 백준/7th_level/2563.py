c=int(input()) #색종이 수 input

arr = [[0] * 100 for _ in range(100)] #전부 0으로 set

for i in range(0,c):
    x,y=map(int,input().split())
    if(x>90 or y>90):
        print("Wrong Area")
        exit(0)

    for j in range(x,x+10):
        for k in range(y,y+10):
            arr[j][k]=1
    
count=0
for i in range(0,100):
    for j in range(0,100):
        if (arr[i][j]!=0):
            count+=1

print(count)