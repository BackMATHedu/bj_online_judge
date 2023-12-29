# 라이브러리 세팅
import sys
input = sys.stdin.readline
# 입력
S = input().strip()
# 구현
    # 알파벳 순서대로 리스트 자료에 등록
list_alphabet = [chr(97+i) for i in range(26)]

result_list =[]
cnt = 0
for i in list_alphabet:
    if i in S:
        result_list.append(S.index(i))
    else:
        result_list.append(-1)
# 결과물 출력
print(*result_list)