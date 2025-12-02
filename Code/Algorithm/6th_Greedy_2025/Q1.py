import sys
input=sys.stdin.readline

def BridgingtheGap(arr_1:list,arr_2:list,amount:int,count:int,cost:int):
    if(len(arr_1)<=0):
        return cost
    
    if(count%2==0): #횟불이 왼쪽에 존재
        arr_1_sort=merge_sort(arr_1)
        if(len(arr_1)<=amount):
            part_cost=0
            for i in arr_1:
                part_cost+=i
            cost+=part_cost
            return cost
        else:
            part_cost=0
            for i in range(0,amount):
                part_cost+=arr_1_sort[i]
            cost+=part_cost
            return BridgingtheGap(arr_1_sort[amount:],arr_1_sort[:amount],amount,count+1,cost)
        
        
    




def combine(a,b):
    arr=[] 
    point_1=0
    point_2=0
    for i in range(len(a)+len(b)):
        if(len(a)<=point_1):
            while(len(b)>point_2):
                arr.append(b[point_2])
                point_2+=1
            break

        if(len(b)<=point_2):
            while(len(a)>point_1):
                arr.append(a[point_1])
                point_1+=1
            break

         #작은 수만 집어 넙기       
        if(a[point_1]>=b[point_2]):
            arr.append(b[point_2])
            point_2+=1

        elif(a[point_1]<b[point_2]):
            arr.append(a[point_1])
            point_1+=1

    return arr

def merge_sort(a):
    if(len(a)<=1):
        return a
    mid=len(a)//2
    return combine(merge_sort(a[:mid]),merge_sort(a[mid:]))

x=list(int,input().split(','))

if(len(x[2:])!=x[0]):
    print("Input error")
    exit(0)

print(BridgingtheGap(x[2:],[],x[1],0,0))
