count=[]
for i in range(0,26): #각각 리스트 카운트 0으로 설정
    count.append(0)

x=list(input())

for i in x:
    if(i == "a" or i == "A"):
        count[0] = count[0] + 1
    elif(i == "b" or i == "B"):
        count[1] = count[1] + 1
    elif(i == "c" or i == "C"):
        count[2] = count[2] + 1
    elif(i == "d" or i == "D"):
        count[3] = count[3] + 1
    elif(i == "e" or i == "E"):
        count[4] = count[4] + 1
    elif(i == "f" or i == "F"):
        count[5] = count[5] + 1
    elif(i == "g" or i == "G"):
        count[6] = count[6] + 1
    elif(i == "h" or i == "H"):
        count[7] = count[7] + 1
    elif(i == "i" or i == "I"):
        count[8] = count[8] + 1
    elif(i == "j" or i == "J"):
        count[9] = count[9] + 1
    elif(i == "k" or i == "K"):
        count[10] = count[10] + 1
    elif(i == "l" or i == "L"):
        count[11] = count[11] + 1
    elif(i == "m" or i == "M"):
        count[12] = count[12] + 1
    elif(i == "n" or i == "N"):
        count[13] = count[13] + 1
    elif(i == "o" or i == "O"):
        count[14] = count[14] + 1
    elif(i == "p" or i == "P"):
        count[15] = count[15] + 1
    elif(i == "q" or i == "Q"):
        count[16] = count[16] + 1
    elif(i == "r" or i == "R"):
        count[17] = count[17] + 1
    elif(i == "s" or i == "S"):
        count[18] = count[18] + 1
    elif(i == "t" or i == "T"):
        count[19] = count[19] + 1
    elif(i == "u" or i == "U"):
        count[20] = count[20] + 1
    elif(i == "v" or i == "V"):
        count[21] = count[21] + 1
    elif(i == "w" or i == "W"):
        count[22] = count[22] + 1
    elif(i == "x" or i == "X"):
        count[23] = count[23] + 1
    elif(i == "y" or i == "Y"):
        count[24] = count[24] + 1
    elif(i == "z" or i == "Z"):
        count[25] = count[25] + 1
    else:
        print("Error")

d=1
c=1
max=count[0]

for i in count: #숫자들 카운트의 가장 큰 값 찾기
    if(i>max):
        max=i
        c=d #max는 가장 많은 수의 개수
    d+=1

same=0

for i in count:
    if(i==max):#만약 가장 큰 값이랑 같은 리스트가 개수가 존재한다면?
        same = same+1

    if(same>=2):    
        print("?")
        exit(0)


if(same==1):
    if(c == 1):
        print("A")
    elif(c == 2):
        print("B")
    elif(c == 3):
        print("C")
    elif(c == 4):
        print("D")
    elif(c == 5):
        print("E")
    elif(c == 6):
        print("F")
    elif(c == 7):
        print("G")
    elif(c == 8):
        print("H")
    elif(c == 9):
        print("I")
    elif(c == 10):
        print("J")
    elif(c == 11):
        print("K")
    elif(c == 12):
     print("L")
    elif(c == 13):
        print("M")
    elif(c == 14):
        print("N")
    elif(c == 15):
        print("O")
    elif(c == 16):
     print("P")
    elif(c == 17):
        print("Q")
    elif(c == 18):
        print("R")
    elif(c == 19):
         print("S")
    elif(c == 20):
        print("T")
    elif(c == 21):
        print("U")
    elif(c == 22):
        print("V")
    elif(c == 23):
        print("W")
    elif(c == 24):
        print("X")
    elif(c == 25):
        print("Y")
    elif(c == 26):
        print("Z")
    else:
        print("Error")
else:
    print("?")