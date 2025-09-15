import time

start = time.time()

s = 0

def input_data(a): #데이터 받아서 2차원 배열에 설정
    arr=[]

    for i in range(0,a):
        age,number=input().split()
        arr.append([age,number])
    return arr
        
def list_sort(data):
    a=len(data)
    new_data=[]
    for i in range(0,201):
        for j in range(0,a):
            if(int(data[j][0])==i):
                new_data.append(data[j])

    return new_data

def print_2D(arr):
    a=len(arr)
    for i in range(0,a):
        print(*arr[i])


x=int(input())

arr=input_data(x)
sort_list=list_sort(arr)
print_2D(sort_list)


end = time.time()

print("걸린 시간:", end - start, "초")