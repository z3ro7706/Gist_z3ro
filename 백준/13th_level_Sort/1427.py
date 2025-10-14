
x=list(map(int, input()))


arr=[] # 숫자 카운트 리스트
for i in range(0,10): #0으로 찬 배열 생성
    arr.append(0)

for i in range(len(x)):
    y=x[i]
    arr[y]+=1

arr_final=[]
for i in range(len(arr)-1,-1,-1):
    for j in range(0,arr[i]):
        arr_final.append(i)

print(*arr_final,sep="")