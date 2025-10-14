def Find(a,b,c,d,e,f):
    g=0
    if(a==c):
        g=e
    elif(a==e):
        g=c
    else:
        g=a

    if(b==d):
        h=f
    elif(b==f):
        h=d
    else:
        h=b
        
    return g,h
    
    


p1x,p1y=map(int,input().split())
p2x,p2y=map(int,input().split())
p3x,p3y=map(int,input().split())
print(*Find(p1x,p1y,p2x,p2y,p3x,p3y))