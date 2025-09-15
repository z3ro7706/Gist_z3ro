import sys

class Stack:  #입구가 막힌 병(선입후출 형태의 데이터 형식)
    def __init__(self):
        self.stack = []  
    
    def push(self, x):  #1번 조건 (데이터 쌓기)
        self.stack.append(x) #들어온 값을 stack형태에 넣음
    
    def pop(self):  #2번 조건 (앞에서 지우고 뽑기)
        if len(self.stack) == 0: #만약 stack의 길이가 0이라면(아무것도 들어있지 않다면)
            return -1 #-1을 반납해라
        return self.stack.pop()#들어있따면, stack의 맨 앞(0)번째 애를 없애고 구조를 return
    
    def top(self):  #5번 조건( 선입후출 )
        if len(self.stack) == 0: #만약 아무것도 없다면
            return -1 #-1 return
        return self.stack[-1] # 있는 경우 맨 뒤의 데이터를 뽑아내기(선입후출)
    
    def __len__(self): #3번 조건(갯수 카웃트)
        return len(self.stack) 

    def empty(self):  #4번 조건
        return 1 if len(self.stack) == 0 else 0 #만약 비어있으면 1, 아니면 0
    
    
if __name__ == "__main__":
    get_line = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input = lambda: int(sys.stdin.readline().strip())

    N = get_input()
    stack = Stack()

    for _ in range(N):
        now_input = list(get_line())
        command = now_input[0]
        
        if command == 1:
            stack.push(now_input[1])
        elif command == 2:
            print(stack.pop())
        elif command == 3:
            print(len(stack))
        elif command == 4:
            print(stack.empty())
        elif command == 5:
            print(stack.top())