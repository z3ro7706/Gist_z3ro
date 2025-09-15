t=int(input()) #받을 정수의 개수

arr=[]
for i in range(0,t):
    word=list(input()) #받은 단어를 list화 
    arr.append(word[0])
    arr.append(word[-1])

for i in range(0,t):
    print(arr[2*i],arr[2*i+1],sep="")





