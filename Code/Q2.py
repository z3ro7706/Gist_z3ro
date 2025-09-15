import sys
import re
input=sys.stdin.readline

def Find_max(l:list):
    max=l[0]
    for i in l:
        if(i>=max):
            max=i

    return max

def LongestWord(sen):
    arr_del=re.findall(r"[A-Za-z0-9]+", sen)
    arr_count=[]
    for i in arr_del:
        arr_count.append(len(i))
    
    key=Find_max(arr_count)
    for i in arr_del:
        if(len(i)==key):
            return i


arr=input().strip()

print(LongestWord(arr))