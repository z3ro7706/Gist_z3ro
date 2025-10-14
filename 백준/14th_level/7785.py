x=int(input()) #출입기록
log_list=set()
for i in range(0,x):
    name,log=input().split()
    if(log=="enter"):
        log_list.add(name)
    elif(log=="leave"):
        log_list.remove(name)
    else:
        print("wrong log")

for i in sorted(log_list,reverse=True):
    print(i)