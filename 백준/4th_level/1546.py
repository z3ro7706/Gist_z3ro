x=int(input()) #받을 정수의 갯수 받기

value=list(map(int, input().split()))
point = 0
max=value[0]
for i in range(len(value)):
    if value[i]>max:
        max = value[i] 
        point = i #최대값 위치 설정

for i in range(len(value)): #새로운 점수로 변경
    value[i]= value[i]/max*100


count=0
for i in range(len(value)):
    count=count + value[i]

avg = count/len(value)
print(avg)
