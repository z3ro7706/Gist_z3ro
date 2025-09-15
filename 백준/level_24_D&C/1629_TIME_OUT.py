import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

def quick_square(input:int,count:int):
    global a,b,c
    if(count>= b):
        return input

    if(2*count<=b): #그 전 값의 제곱값을 해도 범위 내에서 존재
        input=(input*input)%c
        count=2*count
        return quick_square(input,count)
    elif(2*count>=b): #제곱한 경우 범위 내에 존재하지 않을때(즉 증가율이 너무 큰 경우)
        input=(input*a)%c
        count=count+1
        return quick_square(input,count)


print(quick_square(a,1))
