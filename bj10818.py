# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
N = int(input())
num_list = list(map(int, input().split()))

# 구현
print(min(num_list), max(num_list))
# 결과물 출력
