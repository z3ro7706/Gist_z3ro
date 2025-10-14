import sys
input=sys.stdin.readline

n=int(input())

stair_data=[0]*n
stair_data_ans=[0]*n

for i in range(0,n):
    value=int(input())
    stair_data[i]=value

if(len(stair_data)!= n): #debug
    print("Input data error")
    exit(0)

if len(stair_data)<=2:
    print(sum(stair_data))
else:
    stair_data_ans[0]=stair_data[0]
    stair_data_ans[1]=stair_data[0]+stair_data[1]
    for i in range(2,n):
        stair_data_ans[i]=max(stair_data_ans[i-3]+stair_data[i-1]+stair_data[i],stair_data_ans[i-2]+stair_data[i])    
    print(stair_data_ans[-1])