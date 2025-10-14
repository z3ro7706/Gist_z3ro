import sys
input = sys.stdin.readline

n=int(input())
 
count=0
row=[0]*n #list의 위치를 x좌표, 값을 y좌표로 하여서 1차원 배열로 해결(어쩌피 같은 줄에는 1개 밖에 들어가지 못하기 때문)

def is_postible(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i): #같은 줄 or 대각선에 존재하는 경우
            return False 
        
    return True

def n_queens(x):
    global count
    if x==n:
        count+=1
        return
    
    else:
        for i in range(n):
            row[x]=i #queen을 x,i에 놓는다.
            if is_postible(x):
                n_queens(x+1)

n_queens(0)
print(count)