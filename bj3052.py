# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
cache = set()
for _ in range(10):
    num = int(input())

# 구현
    remain = num%42
    cache.add(remain)
    
# 결과물 출력
print(len(cache))