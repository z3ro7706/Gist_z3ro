x=list(input())

for i in range(len(x)):
    if(x[i]!=x[-i-1]):
        print("0")
        exit(0)

print("1")
