def fibonacci(a:int):
    if(a>2):
        return fibonacci(a-1)+fibonacci(a-2)
    elif(a==2):
        return 1
    elif(a==1):
        return 1
    else:
        exit(0)

x=int(input())

print(fibonacci(x))