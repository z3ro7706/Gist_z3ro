import sys
input=sys.stdin.readline

l=int(input())
arr=[]
for i in range(0,l):
    arr.append(list(map(int,input().split())))


count_blue=0
count_white=0

def check_blue(a:list):
    count=0
    for i in a:
        if(i==0):
            pass
        elif(i==1):
            count+=1
        else:
            print("Blue value error")
            exit(0)
    
    if(count!=0):
        return False
    return True

def check_white(a:list):
    count=0
    for i in a:
        if(i==1):
            pass
        elif(i==0):
            count+=1
        else:
            print("White value error")
            exit(0)
    
    if(count!=0):
        return False
    return True


def cut(a:list):
    #종료조건
    if(len(a)<=1):
        return 1
    
    if(check_blue(a) is True):
        count_blue+=1
        
    elif(check_white(a) is True):
        count_white+=1


    value=len(a) #한 변의 길이
    #잘라주는 작업 1개 list 를 4개의 리스트로 변환하여 확장하여 재귀적으로 해결
    arr_new1=[]
    arr_new2=[]
    arr_new3=[]
    arr_new4=[]

    for i in range(0,value//2):
        arr_new1.append(a[0:value//2][i])
        arr_new2.append(a[0:value//2][i+value//2])
        arr_new3.append(a[value//2:value][i])
        arr_new4.append(a[value//2:value][i+value//2])
    
    cut(arr_new1)
    cut(arr_new2)
    cut(arr_new3)
    cut(arr_new4)


cut(arr)
print(count_white)
print(count_blue)