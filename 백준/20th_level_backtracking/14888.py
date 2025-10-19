import sys
input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_value=1e10
max_value=-1e10

def dfs(i,arr):
    global data,add,sub,mul,div,min_value,max_value
    if(i==n):
        max_value=max(max_value,arr)
        min_value=min(min_value,arr)

    else:
        if add>0:
            add-=1
            dfs(i+1,arr+data[i]) #global이므로 add의 갯수가 1개 감소한 상태로 실행됨
            add+=1
        
        if sub>0:
            sub-=1
            dfs(i+1,arr-data[i])
            sub+=1

        if mul>0:
            mul-=1
            dfs(i+1,arr*data[i])
            mul+=1

        if div>0:
            div-=1
            dfs(i+1,int(arr/data[i]))
            div+=1

        
dfs(1,data[0])

print(max_value)
print(min_value)