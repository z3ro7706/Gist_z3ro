import sys
input=sys.stdin.readline

def DFS(graph:list,visted:list,p:int):
    print(p,end=' ')
    visited[p]=True
    for i in graph[p]:
        if not visted[i]:
            DFS(graph,visted,i)

    

n=int(input()) #vertex의 갯수 입력
arr=[[]for _ in range(0,n+1)]

for i in range(1,n+1):
    arr_n=[]
    arr_n=list(map(int,input().split(',')))
    arr[i]=arr_n

visited = [False for _ in range(0,n+1)]

print(DFS(arr,visited,1))