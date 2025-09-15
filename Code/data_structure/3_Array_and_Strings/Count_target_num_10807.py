N = int(input()) #n개의 정수 받기
numbers = list(map(int, input().split())) #중복되는 갯수를 카운트, split을 이용해 함수로 만들기. ex input N = 1,2,3,4,5 -> number = [1,2,3,4,5]

v = int(input()) #target number를 햘당 받는다
print(numbers.count(v)) #함수값에 nubmer 함수를 받고, 이를 같은 갯수를 count함

#O(n) = n