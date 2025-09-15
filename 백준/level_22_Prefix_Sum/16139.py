import sys
input=sys.stdin.readline

word=list(input().strip())

len_word=len(word)+1
word_count=[[0]*len_word for _ in range(27)]

time=int(input())

def count_alphabet(alpabet:str,start:int,end:int):
    num=ord(alpabet)-97
    
    if(word_count[num][-1]!=0): #안에 값이 존재하는 경우
        if(start==0):
            return word_count[num][end]
        else:
            return word_count[num][end]-word_count[num][start-1]
    else: #한번도 탐색하지 않은 경우
        count=0
        num=ord(alpabet)-97
        for i in range(0,len_word-1):
            if(word[i]==alpabet):
                count+=1
            word_count[num][i]=count
        word_count[num][-1]=1
        if(start==0):
            return word_count[num][end]
        else:
            return word_count[num][end]-word_count[num][start-1]
    
for i in range(0,time):
    x, y, z = input().split()

    print(count_alphabet(str(x),int(y),int(z)))
