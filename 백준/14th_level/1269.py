a,b=map(int,input().split())
list_a=input().split()
list_b=input().split()
list_a_set=set(list_a)
list_b_set=set(list_b)
if(len(list_a)!=a or len(list_b)!=b):
    print("Wrong data")
    exit(0)
    
list_ab=list_a_set-list_b_set
list_ba=list_b_set-list_a_set
print(len(list_ab)+len(list_ba))