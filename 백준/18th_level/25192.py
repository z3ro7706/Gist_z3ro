x=int(input())
count=0

name_list=set()
input_data=input()
if(input_data!="ENTER"):
    print("Error")


for i in range(0,x-1):
    input_data=input()
    if(input_data=="ENTER"):
        count=count+len(name_list)
        name_list=set()
    else:
        name_list.add(input_data)

print(len(name_list)+count)