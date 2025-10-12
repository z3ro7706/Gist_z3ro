#각각의 위치까지 가능한 가장 최적의 값을 자신의 위치에 저장 -> 미리 계산을 통해서 계산의 양을 감소시키자는 아이디어 사용?
import sys
input=sys.stdin.readline

def Dynamic_Adventure(arr):
    gap_m=arr[0]
    value_list=arr[1:]

    for i in range(0,len(value_list)):
        arr_exp=[]
        for j in range(1,gap_m+1):
            if(i-j>=0):
                arr_exp.append(value_list[i]+value_list[i-j])
                
        if(len(arr_exp)>=1):
            value_list[i]=MAX(arr_exp)

    return value_list[-1]
        

def MAX(arr):
    max=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]>=max):
            max=arr[i]

    return max


x=list(map(int,input().split()))
print(Dynamic_Adventure(x))
