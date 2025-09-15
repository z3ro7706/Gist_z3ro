score=[]
count=[]
for i in range(0,20):
    n,c,s=input().split()
    c = float(c)
    if(s!="P"):
        score.append(s)
        count.append(c)

tot=0
for i in range(len(count)):
    tot=tot+count[i]

tot_g = 0
for i in range(len(score)):
    if(score[i]=="A+"):
        tot_g+=4.5*count[i]
    if(score[i]=="A0"):
        tot_g+=4.0*count[i]
    if(score[i]=="B+"):
        tot_g+=3.5*count[i]
    if(score[i]=="B0"):
        tot_g+=3.0*count[i]
    if(score[i]=="C+"):
        tot_g+=2.5*count[i]
    if(score[i]=="C0"):
        tot_g+=2.0*count[i]
    if(score[i]=="D+"):
        tot_g+=1.5*count[i]
    if(score[i]=="D0"):
        tot_g+=1.0*count[i]
    if(score[i]=="F"):
        tot_g+=0*count[i]

print(tot_g/tot)

    