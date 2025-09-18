import sys
from collections import deque
N = int(sys.stdin.readline().strip())

left_arr = []
arr = deque(sorted([int(sys.stdin.readline().strip()) for _ in range(N)]))

sum = 0

while arr:
    if arr[0] <= 0:
        left_arr.append(arr.popleft())
    elif arr[0] == 1:
        sum += 1
        arr.popleft()
    else:
        break

right_arr = sorted(list(arr), reverse=True)

left_len = len(left_arr) // 2
right_len = len(right_arr) // 2


for i in range(left_len):
    sum += left_arr[2 * i] * left_arr[2 * i + 1]

for j in range(right_len):
    sum += right_arr[2 * j] * right_arr[2 * j + 1]
    
if len(left_arr) % 2:
    sum += left_arr[-1]
if len(right_arr) % 2:
    sum += right_arr[-1]

print(sum)