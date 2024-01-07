# 라이브러리 세팅
import sys
input = sys.stdin.readline
# 입력
N = int(input()) #분해합
# 구현
    #생성자 구하기
num_test = 1
cache = set()
while num_test != N:
    result = num_test
    str_test = str(num_test)
    for i in str_test:
        result += int(i)
    if result == N:
        cache.add(num_test)
    num_test += 1
# 결과물 출력
if cache == set():
    print(0)
else:
    print(min(cache))