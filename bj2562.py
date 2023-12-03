# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력 및 구현
max = float("-inf") # max 기본값을 -infinite로 세팅
for i in range(9):
    num_input = int(input())
    if num_input >= max: # max보다 크거나 같은 경우에 max을 변경하고 index 저장
        max = num_input
        index = i+1

# 결과물 출력
print(max)
print(index)