import sys

class Node: #class Node에서의 정의
    def __init__(self, key=None): #self의 의 key값을 받는경우 (key는 아무것도 없는 None상태)
        self.prev = None #prev를 받은 key값
        self.next = None #next를 받은 key값으로 지정
        self.key = key #자기 자신으로 정의한다.

class DoublyLinkedList: #doulylinkedlist에서의 정의
    def __init__(self):
        self.head = Node()  #비운 노드
        self.tail = Node()  #비운 노드

        self.head.next = self.tail #head의 다음 노드를 꼬리로 잡는다
        self.tail.prev = self.head # tail의 이전노드를 머리로 잡는다. 
        #이를 통해서 원형 순환구조를 구현(using doublylinkedlist)
        
        self.size = 0  

    def splice(self, a, b, x):  # O(1) (함수, 시작하는 위치, 끝나는 노드, 삽입되는 노드) ->원형적으로 돌며 삽입되는 위치가 달라지기 때문
        if a is None or b is None or x is None: #만약 a가 비었거나, b가 비엇거나, x가 비었다면 return 시키기
            return  

        ap = a.prev #ap는 a라는 Node객체의 prev값(블록 전 노드)
        bn = b.next #bn는 b라는 Node객체의 next값(블록 후 노드)
        xn = x.next #xn는 x라는 Noderorcpdml 다음값(삽입 지점 뒤 노드)

        #꼬리가 꼬리는 무는 형태로 구성
        if ap: #만약 ap가 Node가 아니라면 실행
            ap.next = bn #ap의 다음노드를 bn으로 잡는다.
        if bn: #만약 bn이 Node가 아니라면 실행
            bn.prev = ap  #bn 전의 노드를 ap로 잡아준다.

        a.prev = x #a의 전 노드를 x라 지정한다. 
        b.next = xn #b의 다음 노드를 xn이라 구성한다. 
        if x: #만약 x가 None이 아니라면.
            x.next = a #x의 다음노드를 a로 지정한다. 
        if xn:
            xn.prev = b

    def moveAfter(self, a, x):  # O(1)
        self.splice(a, a, x)

    def moveBefore(self, a, x):  # O(1)
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):  # O(1)
        new_node = Node(key)
        self.moveAfter(new_node, x)
        self.size += 1

    def insertBefore(self, x, key):  # O(1)
        new_node = Node(key)
        self.moveBefore(new_node, x)
        self.size += 1

    def pushFront(self, key):  # O(1)
        self.insertAfter(self.head, key)

    def pushBack(self, key):  # O(1)
        self.insertBefore(self.tail, key)

    def search(self, key):  # O(n)
        node = self.head.next
        while node != self.tail:
            if node.key == key:
                return node
            node = node.next
        return None

    def remove(self, x):  # O(1)
        if x is None or x == self.head or x == self.tail:
            return None
        
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1  # 크기를 감소시킴

    def popFront(self):  # O(1)
        if self.head.next == self.tail: 
            return None
        else:
            value = self.head.next.key
            self.remove(self.head.next)
            return value

    def popBack(self):  # O(1)
        if self.head.next == self.tail:  
            return None
        else:
            value = self.tail.prev.key
            self.remove(self.tail.prev)
            return value

    def printList(self):  
        current = self.head.next
        while current != self.tail:
            print(current.key, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    L = DoublyLinkedList()
    for i in range(1, N + 1):
        L.pushBack(i)

    print("<", end="")
    while L.size != 0:
        for j in range(K - 1):
            L.pushBack(L.popFront())
        print(L.head.next.key, end="")
        L.popFront()
        if L.size != 0:
            print(", ", end="")

    print(">", end="")

       #O(NK)