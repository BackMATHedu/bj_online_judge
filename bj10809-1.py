# 라이브러리 세팅
import sys
input = sys.stdin.readline
# 입력
S = input().strip()
# 구현
    # 알파벳 순서대로 사전형 자료에 등록
dict_result = {}
for i in range(26):
    dict_result[chr(97+i)] = -1

cnt = 0
for i in S:
    if dict_result[i] == -1:
        dict_result[i] = cnt
    cnt += 1
# 결과물 출력
print(*[dict_result[chr(97+i)] for i in range(26)])