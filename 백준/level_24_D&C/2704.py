import sys
input=sys.stdin.readline

a,b=map(int,input().split()) 
matrix_one=[]
for i in range(0,a):
    arr=list(map(int,input().split()))
    if(len(arr)!=b):
        print("list input error")
        exit(0)
    matrix_one.append(arr)


c,d=map(int,input().split()) 


matrix_two=[]
for i in range(0,c):
    arr=list(map(int,input().split()))
    if(len(arr)!=d):
        print("list input error")
        exit(0)
    matrix_two.append(arr)

C = [[0 for _ in range(d)] for _ in range(a)]

for n in range(a):
    for k in range(d):
        for m in range(b):
            C[n][k]+=matrix_one[n][m]*matrix_two[m][k]


for i in C:
    for j in i:
        print(j,end=' ')
    print()