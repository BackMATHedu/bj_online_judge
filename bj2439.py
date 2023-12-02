import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 실행 코드 및 결과물 출력
for i in range(N):
    print(" "*(N-(i+1))+"*"*(i+1))