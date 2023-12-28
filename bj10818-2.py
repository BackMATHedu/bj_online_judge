# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 구현
num_min = float('inf')
num_max = float('-inf')

for i in map(int, input().split()):
    if i >= num_max:
        num_max = i
    if i <= num_min:
        num_min = i
# 결과물 출력
print(num_min, num_max)