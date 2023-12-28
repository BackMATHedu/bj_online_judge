# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
strings = list(map(int,input().split()))
# 구현
if strings == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif strings == [8,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')
# 결과물 출력