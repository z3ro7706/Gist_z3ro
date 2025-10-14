arr=[[0] * 9 for _ in range(9)]
max=0
x=0
y=0

for i in range(0,9):
    insert=list(map(int,input().split()))
    for j in range(0,9):
        for k in insert:
            if(k<0 or k>=100):
                exit(0)

        arr[i][j]=insert[j]
        count=1
        for l in insert:
            
            if(l>=max):
                max=l
                x=i+1 #위치
                y=count
                count+=1
            else:
                count+=1

                

print(max)
print(x, y)