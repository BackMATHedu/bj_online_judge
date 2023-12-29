# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
T = int(input())
# 구현
for _ in range(T):
    result = 0
    score = 1
    sentence = input().strip()
    for i in sentence:
        if i == 'O':
            result += score
            score += 1
        else:
            score = 1
# 결과물 출력
    print(result)