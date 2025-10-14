x=int(input()) #amount of total sugar

y=x//5 #max of 5kg

for i in range(0,y+1):
    if((x-(y-i)*5)%3==0):
        print(int(y-i+((x-(y-i)*5)/3)))
        exit(0)

print("-1")