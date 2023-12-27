# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
H, M = map(int, input().split())

# 구현
    # 45분 이후인 경우
if M >= 45:
    result_M = M-45
    result_H = H
    # 45분 이전인 경우
else:
    result_M = M+60-45
    # 시간이 0시인 경우와 그 외인 경우로 나눔.
    if H == 0:
        result_H = 23
    else:
        result_H = H-1

# 결과물 출력
print(result_H, result_M)