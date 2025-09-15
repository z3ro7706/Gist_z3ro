n,m=map(int,input().split()) 
arr=[]

def back():
    if(len(arr) == m):
        print(" ".join(map(str,arr)))
        return
    
    for i in range(1,n+1): #1~n까지 탐색하기 위함
        if i not in arr:
            arr.append(i)
            back()
            arr.pop() #return 으로 인해서 돌아왔을때, 만약 꽉 차 있는 경우 하나를 꺼내서 바로 전 상태로 이끌어감       

back()


