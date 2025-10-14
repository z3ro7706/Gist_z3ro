
x=int(input()) #test case

def check_parenthesis(arr:list):
    count=1
    for i in arr:
        if(i=="("):
            count+=1
        elif(i==")"):
            count-=1
        
        if(count<=0):
            return False
        
    if(count==0):
        return False
    elif(count==1):
        return True
    else:
        return False   
        
for i in range(0,x):
    parenthesis=list(input())

    if(check_parenthesis(parenthesis) is True):
        print("YES")
    elif(check_parenthesis(parenthesis) is False):
        print("NO")
    else:
        print("WTF?")

