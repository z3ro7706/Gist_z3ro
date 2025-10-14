x,y=map(int, input().split()) #x는 바구니 갯수, m은 공을 넣는 횟수
if(x<=0 or x>100 or y<0 or y>100):
    exit(0)

arr=[]
for i in range(0,x):
    arr.append(0)

for i in range(0,y):
    n1, n2, n3=map(int, input().split())
    for i in range(n1-1, n2):
        arr[i]=n3

print(*arr)