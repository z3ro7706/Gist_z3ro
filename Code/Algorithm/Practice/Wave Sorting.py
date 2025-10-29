import sys
input=sys.stdin.readline

def WaveSorting(arr:list):
    counting_list=[]
    for i in range(0,len(arr)):
        count=0
        for j in range(0,len(arr)):
            if(arr[i]==arr[j]):
                count+=1

        counting_list.append(count)

    if(find_max(counting_list)>(len(arr)//2)):
        return False
    else:
        return True    



def find_max(arr:list):
    max=arr[0]
    for i in range(0,len(arr)):
        if(max<=arr[i]):
            max=arr[i]
    return max

x=list(map(int,input().split(',')))
print(WaveSorting(x))