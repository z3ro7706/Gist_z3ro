list_1=list(input())
list_2=list(input())
list_3=list(input())
list_4=list(input())
list_5=list(input())
#받은 5줄 list화

a=max(len(list_1),len(list_2),len(list_3),len(list_4),len(list_5)) 
#리스트 길이 중 가장 긴 길이(반복횟수)

for i in range(a):
    if i < len(list_1):
        print(list_1[i], end="")
    if i < len(list_2):
        print(list_2[i], end="")
    if i < len(list_3):
        print(list_3[i], end="")
    if i < len(list_4):
        print(list_4[i], end="")
    if i < len(list_5):
        print(list_5[i], end="")

        
