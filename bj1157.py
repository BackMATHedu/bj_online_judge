# 라이브러리 세팅
import sys
input = sys.stdin.readline
# 입력
S = input().strip()
# 구현
dict_result = {}
for i in range(26):
    dict_result[chr(65+i)] = 0

S = S.upper()
    # 알파벳 나올 때마다 카운팅 추가
for i in S:
    dict_result[i] += 1

max_cnt = float('-inf')
result = ''
flag = 0
for i in list(dict_result.keys()):
    if max_cnt < dict_result[i]:
        max_cnt = dict_result[i]
        result = i
        flag = 0
    elif max_cnt == dict_result[i]:
        flag = 1
# 결과물 출력
if flag == 1:
    print('?')
else:
    print(result)