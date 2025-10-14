x=int(input()) #받을 데이터 개수
arr=input().split()
if(len(arr)!=x): #받은 데이터 개수와 실제 개수가 다르다면 종료
    print("Data count error")
    exit(0)

count_list=[] #2차원 배열로 구성 [실제 숫자, 작은 숫자 개수]
for i in range(0,x):
    count_list.append([arr[i],0])
    
for i in range(0,x):
    search=arr[i] #탐색하고자 하는 수
    for j in range(0,x):
        if(count_list[j][0]<arr[i]):
            count_list[i][1]+=1

for i in range(0,x):
    print(count_list[i][1],end=" ")
