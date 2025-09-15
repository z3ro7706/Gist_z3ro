x=int(input())
h_list={}
idata=input().split()
for i in range(0,x):
    if(idata[i] not in h_list):
        h_list[idata[i]]=1
    else:
        h_list[idata[i]]+=1

y=int(input())
check_list=input().split()



arr=[]
for i in range(0,y):
    if(check_list[i] not in h_list):
        arr.append("0")
    else:
        arr.append(h_list[check_list[i]])


print(*arr)