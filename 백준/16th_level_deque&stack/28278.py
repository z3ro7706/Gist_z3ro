y=int(input()) #받는 명령어 개수
arr=[]
print_list=[]
for i in range(0,y):
    x=list(map(int,input().split()))
    if(x[0]==1):
        arr.append(x[1])
    elif(x[0]==2):
        if(len(arr)==0):
           print_list.append(-1)
        else:
            print_list.append(arr[-1])
            arr.pop()
    elif(x[0]==3):
        print_list.append(len(arr))
    elif(x[0]==4):
        if(len(arr)==0):
            print_list.append(1)
        else:
            print_list.append(0)
    elif(x[0]==5):
        if(len(arr)==0):
            print_list.append(-1)
        else:
            print_list.append(arr[-1])
    else:
        print("error")


for i in print_list:
    print(i)