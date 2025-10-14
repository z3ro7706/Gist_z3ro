x=int(input())
door_list=set()
for i in range(2,x+1):
    j=1
    while(1):
        if(i*j>x):
            break
        if(i*j in door_list):
            door_list.remove(i*j)
        else:
            door_list.add(i*j)
        j+=1
    
print(x-len(door_list))