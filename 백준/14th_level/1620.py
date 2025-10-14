x,y=map(int,input().split())
dictionary_int={} #dict로 선언
dictionary_string={} 
for i in range(0,x):
    slave=input()
    dictionary_int[i+1]=slave
    dictionary_string[slave]=i+1

arr=[]
for i in range(0,y):
    slave_list=input()
    if(slave_list.isdigit()):
        arr.append(dictionary_int[int(slave_list)])
    else:
        arr.append(dictionary_string[slave_list])

for i in arr:
    print(i)

"""
try:
        cmd = int(cmd)
        print(poke[cmd-1])
    except ValueError:
        print(poke_reverse[cmd]+1)
"""