import sys
input=sys.stdin.readline

def CodelandUsernameValidation(w):
    arr=list(str(w))

    if(len(arr)<4 or len(arr)>25):
        return "false"

    if('a'>arr[0] or arr[0] >'z'):
        return "false"

    if(arr[-1]=="_"):
        return "false"

    for i in arr:
        if not (i.isalnum or i == "_"):
            return "false"
        
    return "true"


x=input().strip()
print(CodelandUsernameValidation(x))