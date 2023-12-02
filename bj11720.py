import sys
input = sys.stdin.readline

# 입력
N = int(input())
array_num = input().strip()

# 실행 코드
result = 0
for i in array_num:
    result += int(i)

# 결과물 출력
print(result)