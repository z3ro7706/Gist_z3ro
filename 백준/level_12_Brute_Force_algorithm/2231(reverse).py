def Digit_Generator(x:int):
    y=list(str(x))
    count=0
    for i in y:
        count=count+int(i)
    
    return count+x
    
a=int(input())
print(Digit_Generator(a))
        