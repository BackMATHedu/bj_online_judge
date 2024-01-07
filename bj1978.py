# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
N = int(input())
set_input = set(map(int, input().split()))
# 구현

max_input = max(set_input)
set_prime = set(range(2, max_input + 1))
for i in range(2, max_input + 1):
    if i in set_prime:
        # 에라토스네테스의 체
        set_prime -= set(range(2 * i, max_input + 1, i))

result_set = set_input & set_prime
# 결과물 출력
print(len(result_set))