# 라이브러리 세팅
import sys
input = sys.stdin.readline
# 입력
while True:
    list_side = sorted(list(map(int, input().split())))
    #print(list_side)
# 구현
    if (list_side[0], list_side[1], list_side[2]) == (0, 0, 0):
        break
    else:
        if list_side[2]**2 == (list_side[0]**2) + (list_side[1]**2):
            print('right')
        else:
            print('wrong')
# 결과물 출력