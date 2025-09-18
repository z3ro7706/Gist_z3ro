import sys
input=sys.stdin.readline

def ConsonantCount(w):
    word = list(str(w))

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "u"," "]
    arr_find=[]
    for i in word:
        if 'A'<=i<='z':
            if(i not in vowels):
                arr_find.append(i)
            
        
    return len(arr_find)

x=input().strip()
print(ConsonantCount(x))
