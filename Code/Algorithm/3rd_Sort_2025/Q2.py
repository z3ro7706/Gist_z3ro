import sys
input=sys.stdin.readline


count_list=[]
def WaveSorting(arr):
    for i in range(0,len(arr)):
        count=0
        for j in range(0,len(arr)):
            if(arr[i]==arr[j]):
                count+=1
        count_list.append(count)               

    if(find_max(count_list)>((len(arr))//2)):
        return "false"
    else:
        return "true"


def find_max(arr):
    max=arr[0]
    for i in arr:
        if(i>=max):
            max=i
    return max


print(WaveSorting(input()))