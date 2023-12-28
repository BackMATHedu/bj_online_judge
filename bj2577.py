# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
A = int(input())
B = int(input())
C = int(input())

# 구현
    # 사전형으로 10진수 등록
dict_count = {}
for i in range(10):
    dict_count[i] = 0
    # 문자열로 바꿔서 자릿수마다 10진수 cnt 추가
num_product = A*B*C
for i in str(num_product):
    dict_count[int(i)] += 1
    
# 결과물 출력
for i in dict_count.keys():
    print(dict_count[i])