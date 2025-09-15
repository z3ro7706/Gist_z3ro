list_2=["A","B","C"]    #3
list_3=["D","E","F"]    #4
list_4=["G","H","I"]    #5
list_5=["J","K","L"]    #6
list_6=["M","N","O"]    #7
list_7=["P","Q","R","S"]    #8
list_8=["T","U","V"]    #9
list_9=["W","X","Y","Z"] #10
list_0=[] #11


a=list(input())
time=0
for i in range(len(a)):
    if a[i] in list_2:
        time=time+3
    elif a[i] in list_3:
        time=time+4
    elif a[i] in list_4:
        time=time+5
    elif a[i] in list_5:
        time=time+6
    elif a[i] in list_6:
        time=time+7
    elif a[i] in list_7:
        time=time+8
    elif a[i] in list_8:
        time=time+9
    elif a[i] in list_9:
        time=time+10
    else:
        time=time+2

print(time)