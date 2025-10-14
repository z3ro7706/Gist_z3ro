def check_reduplication(arr):
    new_arr=[]
    for i in arr:
        count=0
        for j in new_arr:
            if(j==i):
                count+=1
        if(count==0):
            new_arr.append(i)
    return new_arr

def card_count(a:int, b:list, c:int, d:list):
    arr=[]
    for i in range(0,c): #0으로 초기화
        arr.append(0)

    for i in range(0,c):
        for j in b:
            if(d[i]==j):
                arr[i]+=1
    
    return arr



n=int(input())
Have_list=list(map(int, input().split()))
m=int(input())
Find_list=list(map(int, input().split()))

#DEBUGIN
if(n!=len(Have_list) or m!=len(Find_list)): #잘못된 양의 데이터를 받음
    print("Wrong Data")
    exit(0)

if(m<0 or m>500000 or n<0 or n>500000): #잘못된 양의 데이터를 받음
    print("Wrong Card amount")
    exit(0)

for i in Have_list: #잘못된 데이터 범위
    if(i>10000000 or i<-10000000):
        print("Wrong input list value")

for i in Find_list: #잘못된 데이터 범위
    if(i>10000000 or i<-10000000): 
        print("Wrong Find list value")

if(n!=len(check_reduplication(Have_list))):
   print("Have a reduplicaition of have list")
   exit(0)

if(m!=len(check_reduplication(Find_list))):
   print("Have a reduplicaition of Find list")
   exit(0)


#main 
count_card=card_count(n,Have_list,m,Find_list)
print(*count_card)