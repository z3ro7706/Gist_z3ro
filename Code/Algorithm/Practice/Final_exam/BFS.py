import sys
input=sys.stdin.readline

from collections import deque

def BFS(graph:list, start:int, vistited:list):
    queue = deque([start]) #queue에 시작할 값을 넣어주기
    vistited[start]=True # 처음 시작 부분은 방문하였으므로, 방문처리

    while queue: #queue값이 존재할 때 까지 반복
        v=queue.popleft() #리스트에서 하나 뽑기
        print(v, end=' ') # 출력
        for i in graph[v]: # v와 연결된 그래프에서
            if not vistited[i]:
                queue.append(i) #queue에 넣고
                vistited[i]=True #방문처리

n=int(input()) #vertex의 갯수 입력
arr=[[]for _ in range(0,n+1)]

for i in range(1,n+1):
    arr_n=[]
    arr_n=list(map(int,input().split(',')))
    arr[i]=arr_n

visited = [False for _ in range(0,n+1)]

BFS(arr,1,visited)