import sys
input=sys.stdin.readline

def RemoveBrackets(str):
    arr=list(str)
    count_brackets=0
    error=0
    for i in range(0,len(arr)):
        if(count_brackets<=0):
            if(arr[i]==")"):
                error+=1
                count_brackets+=1

        if(arr[i]=="("):
            count_brackets+=1
        
        if(arr[i]==")"):
            count_brackets-=1
        
        
    return error + count_brackets


print(RemoveBrackets(input()))