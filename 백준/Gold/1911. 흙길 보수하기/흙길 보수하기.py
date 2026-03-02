import sys

N,L = map(int, sys.stdin.readline().strip().split())

waters = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

waters.sort()
result = 0
last_bridge = -1
for left, right in waters:
    left = max(left, last_bridge)

    gap = right - left
    nums = gap // L
    if (gap % L > 0):
        nums += 1

    last_bridge = left + nums * L 
    result += nums


print(result)