x=int(input())

def factorial(a:int):
    if(a>1):    
        return factorial(a-1)*a
    else:
        return 1

print(factorial(x))