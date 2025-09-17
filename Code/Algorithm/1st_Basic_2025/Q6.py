import sys
input=sys.stdin.readline

def LetterCapitalize(s:str):
    return(s[0].upper() + s[1:])


x=list(input().split())
for i in x:
    print(LetterCapitalize(i),end=" ")


