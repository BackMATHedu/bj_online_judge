import sys
input = sys.stdin.readline

N = int(input())
array_num = input().strip()

result = 0
for i in array_num:
    result += int(i)

print(result)