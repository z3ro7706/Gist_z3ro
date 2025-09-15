import sys
input=sys.stdin.readline

n,b=map(int,input().split())

matrix=[]

for i in range(n):
    arr=list(map(int,input().split()))
    if(len(arr)!=n):
        print("Input data error")
        exit(0)
    matrix.append(arr)

def multi(a,b):
    X = [[0]*n for _ in range(n)]
    for i in range(n): # 행렬
        for j in range(n):
            for k in range(n):
                X[i][j] += a[i][k]*b[k][j] % 1000 #곱셈 연산
    return X

def square(x,n): #분할 정복을 이용해 요구 사항만큼 제곱하기
    if n == 1:
        return x
    temp = square(x,n//2)
    if n % 2 == 0 :
        return multi(temp,temp)
    else : 
        return multi(multi(temp,temp),x)
    
value=square(matrix,b)

for i in range(n):
    for j in range(n):
        value[i][j]=value[i][j]%1000

for i in value:
    print(*i)