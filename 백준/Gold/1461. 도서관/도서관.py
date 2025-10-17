import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
right_arr = list(map(int, sys.stdin.readline().strip().split()))

right_arr.sort()
right_arr = deque(right_arr)
left_arr = deque()
answer = []
result = 0
while right_arr:
    pop_val = right_arr.popleft()
    if pop_val < 0:
        left_arr.appendleft(pop_val)
    else:
        right_arr.appendleft(pop_val)
        break

for i in range(len(right_arr) - 1, -1, -M):
    answer.append(right_arr[i])

for i in range(len(left_arr) - 1, -1, -M):
    answer.append(-left_arr[i])


answer.sort(reverse=True)


result += answer[0]
for i in range(1, len(answer)):
    result += answer[i] * 2


print(result)
