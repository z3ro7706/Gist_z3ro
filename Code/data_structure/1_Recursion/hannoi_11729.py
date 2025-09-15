import sys

N = int(sys.stdin.readline().rstrip())

print(2 ** N - 1) #최소 이동 횟수

def move_disk(disk_num, start_peg, end_peg):
    print(f"{start_peg} {end_peg}") #이동 (몇번째 칸 에서 다른 칸으로 이동을 보여줌), 과정을 보여주는 출력시스템

def hanoi(num_disks, start_peg, end_peg):   #디스크 갯수, 시작지점, 목표지점을 받아냄, 이를 재귀적으로 계속해서 반복함
    if num_disks == 1: #만약 디스크가 1개라면
        return move_disk(num_disks, start_peg, end_peg) #위에 movedis를 이용해서 출력 (1,3)이 출력됨
    
    mid_peg = (6 - start_peg - end_peg) #기둥의 합은 항상 1+2+3으로 6이므로, 이를 통해 남은 peg의 번호를 알 수 있음

    hanoi(num_disks-1, start_peg, mid_peg) #n번쨰에 도달하려면 n-1번째에서 나머지가 목표 peg가 아닌 다른 peg 즉 mid peg에 도달해야한다.
    move_disk(num_disks, start_peg, end_peg) #이동과정을 출력하기
    hanoi(num_disks-1, mid_peg, end_peg) #mid peg에 있는 것을 출발 peg, 목표피기는 그대로 지정함 (다시 원래의 형태로 돌려놓기), 시작지점이 바뀜에 주의하자.
    
hanoi(N, 1, 3) #n개의 원판을 1번 peg에서 3번 peg로 이동하게 하자

#O(n) = 2^n