import sys
input=sys.stdin.readline

x,y=map(int,input().split())


arr=[]

for i in range(1,x+1): #list 생성
    arr.append(i)

point=0
print_list=[]
while(1):
    z=(point+y-1)%len(arr)
    print_list.append(arr[z])
    arr.remove(arr[z])
    point=z
    if(len(arr)==0):
        break

print(f"<{', '.join(map(str, print_list))}>")