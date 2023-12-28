# 라이브러리 세팅
import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
# 구현
    cnt_room = 0
    while N > 0:
        N = N - H
        cnt_room += 1
    cnt_stair = N + H
# 결과물 출력
    if cnt_room >= 10:
        print(str(cnt_stair)+str(cnt_room))
    else:
        print(str(cnt_stair)+'0'+str(cnt_room))