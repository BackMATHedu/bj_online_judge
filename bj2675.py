# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
# 구현
    N, strings = input().split()
    N = int(N)
    result = ''
    for i in strings:
        result += i*N
# 결과물 출력
    print(result)