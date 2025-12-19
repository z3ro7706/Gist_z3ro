def DFS(graph:list, start:int):
    n_visted, visted=list(), list()
    n_visted.append(start)

    while n_visted:
        node=n_visted.pop()
        if node not in visted:
            visted.append(node)
            n_visted.extend(graph[node])

    return visted

n=int(input()) #vertex의 갯수 입력
arr=[[]for _ in range(0,n+1)]

for i in range(1,n+1):
    arr_n=[]
    arr_n=list(map(int,input().split(',')))
    arr[i]=arr_n

visited = [False for _ in range(0,n+1)]

print(DFS(arr,1))