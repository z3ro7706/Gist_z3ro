n,m=map(int,input().split())

arr=[]

def back_duplication():
    if(len(arr)==m):
        print(" ".join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        arr.append(i)
        back_duplication()
        arr.pop()

back_duplication()
