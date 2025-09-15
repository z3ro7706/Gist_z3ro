"""
조건
1. 가로 새로 9칸에 숫자가 겹치면 안됨
2. 3*3 칸 안에서 숫자가 1~9까지 겹치면 안됨
-> 이 3가지 조건을 종료조건으로 생성하기(이런 경우 backtracking 실시)
-> 비어 있는 칸에 숫자를 넣어서 되돌아 와야 하니, 빈 숫자 칸 위치를 찾는 리스트 생성
:하나의 케이스만 출력하면 되므로, 모든 빈 공간이 없엇지면 출력하고 함수를 exit으로 강제 종료
"""

def row(a,n): #가로에 넣고자 하는 값이 있는지 확인하는 경우
    for i in range(0,9):
        if n==sudoku[a][i]:
            return False
    return True

def column(a,n):
    for i in range(0,9):
        if n==sudoku[i][a]:
            return False
    return True

def square(y,x,n): #3*3 칸에 넣고자 하는 n이 존재하는지 확인
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3*3+i][x//3*3+j]: #무조건 1,4,7칸부터 탐색하도록 설정
                return False
    return True

def find(n):
    if n==len(blank):#빈 공간만큼 사용되었다면
        for i in sudoku: #줄만큼 출력함
            print(*i)
        exit(0)

    for i in range(1,10):
        y=blank[n][0]