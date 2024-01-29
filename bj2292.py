# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 구현
# 결과물 출력
if N == 1:
    print(1)
else:
    flag = 0
    n = 1
    while flag == 0:
        if (3*n*(n-1))+1 <= N <= 3*n*(n+1)+1:
            flag = 1
        else:
            n += 1
    print(n+1)