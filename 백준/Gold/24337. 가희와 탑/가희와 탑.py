import sys
from collections import deque
N, a, b = map(int, sys.stdin.readline().strip().split())

result = deque()

if a + b > N + 1:
    print(-1)
    exit(0)

left_temp = deque()
right_temp = deque()


if a > b:
    for i in range(a):
        left_temp.append(i+1)
    
    for i in range(b-1):
        right_temp.appendleft(i+1)
else:
    for i in range(a-1):
        left_temp.append(i+1)
    for i in range(b):
        right_temp.appendleft(i+1)


result.extend(left_temp)
result.extend(right_temp)

result = list(result)

extra = N - len(result)

if a == 1:
    result = [result[0]] + [1] * extra + result[1:]
else:
    result = [1] * extra + result


for val in result:
    print(val, end=" ")