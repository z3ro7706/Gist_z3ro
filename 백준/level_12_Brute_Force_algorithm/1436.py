x=int(input())
b=665
count=0
while(1):
    b+=1
    a=list(map(int, str(b)))

    for i in range(len(a)-2):
        if(a[i]==a[i+1]==a[i+2]==6):
            count+=1
            if count==x:
                print(b)
                exit(0)
            break
        
    
   
    