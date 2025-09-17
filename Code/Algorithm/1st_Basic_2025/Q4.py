import sys
input=sys.stdin.readline

def LetterChanges(str):
    if 'a'<=str<='z':
        if(str=='z'):
            return 'A'
        if(chr(ord(str)+1)=='a'):
            return 'A'
        elif(chr(ord(str)+1)=='e'):
            return 'E'
        elif(chr(ord(str)+1)=='i'):
            return 'I'
        elif(chr(ord(str)+1)=='o'):
            return 'O'
        elif(chr(ord(str)+1)=='u'):
            return 'U'
        
        return chr(ord(str)+1)
    else:
        return str
    



arr=list(input().strip())

for i in arr:
    print(LetterChanges(i),end='')