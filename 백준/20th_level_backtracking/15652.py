

n,m=map(int,input().split())
arr=[]

def back_upper():
    if(len(arr)==m):
        print(" ".join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        count=0
        for j in arr:
            if(i<j):
                count+=1
        if(count==0):
            arr.append(i)
            back_upper()
            arr.pop()

back_upper()
