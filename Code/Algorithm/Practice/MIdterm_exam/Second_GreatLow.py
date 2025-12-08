import sys
input=sys.stdin.readline

def SecondGreatLow(arr:list):
    if(len(arr)<=0):
        print("Input data Error")
        exit(0)
    
    arr_set=set(arr)
    arr_n=list(arr_set)

    if(len(arr_n)==1):
        val=[arr_n[0]]+[arr_n[0]]
        return val
        
    
    for i in range(0,len(arr_n)):
        min=i
        for j in range(i,len(arr_n)):
            if(arr_n[min]>arr_n[j]):
                min=j
        if(min!=i):
            arr_n[i],arr_n[min]=arr_n[min],arr_n[i]

    val=[arr_n[1]]+[arr_n[-2]]
    return val

x=list(map(int,input().split(',')))
print(*SecondGreatLow(x))