# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
N = int(input())
array_num = input().strip()

# 구현
result = 0
for i in array_num:
    result += int(i)

# 결과물 출력
print(result)