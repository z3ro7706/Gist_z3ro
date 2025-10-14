import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
count_a=0
count_b=0
count_c=0

def cut_count(x,y,n):
    global count_a,count_b,count_c
    check=arr[x][y]
    
    value=0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=arr[i][j]:
                value=-1
                break
    n=n//3
    if(value==-1):
        cut_count(x,y,n)
        cut_count(x,y+n,n)
        cut_count(x,y+2*n,n)
        cut_count(x+n,y,n)
        cut_count(x+n,y+n,n)
        cut_count(x+n,y+2*n,n)
        cut_count(x+2*n,y,n)
        cut_count(x+2*n,y+n,n)
        cut_count(x+2*n,y+2*n,n)
    else:
        if(check==-1):
            count_a+=1
        elif(check==0):
            count_b+=1
        else:
            count_c+=1

cut_count(0,0,n)
print(count_a)
print(count_b)
print(count_c)
    

