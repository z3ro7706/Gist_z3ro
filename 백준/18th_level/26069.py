x=int(input())
dance_list=set()
dance_list.add("ChongChong")
for i in range(0,x):
    name=list(input().split())
    if(len(name)!=2):
        print("name error")

    if(name[0] in dance_list):
        dance_list.add(name[1])
    elif(name[1] in dance_list):
        dance_list.add(name[0])

print(len(dance_list))