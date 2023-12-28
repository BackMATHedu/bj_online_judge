# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
# 구현
    if N%H == 0:
        num_room = N//H
        num_stair = H
    else:
        num_room = N//H + 1
        num_stair = N%H
# 결과물 출력
    if num_room >= 10:
        print(str(num_stair)+str(num_room))
    else:
        print(str(num_stair)+'0'+str(num_room))