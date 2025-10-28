import sys
from collections import deque

N = int(sys.stdin.readline().strip())
weights = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().strip().split()))

weights.sort(reverse=True)
weights_idxes = [deque() for _ in range(len(weights))]
boxes.sort(reverse=True)


if boxes[0] > weights[0]:
    print(-1)
    exit(0)

idx = 0

for i in range(len(weights)):
    while idx < len(boxes) and weights[i] < boxes[idx]:
        idx += 1

    if idx < len(boxes):
        for j in range(idx, len(boxes)):
            weights_idxes[i].append(j)


T = 0
while True:
    for i in range(len(weights)):
        while weights_idxes[i]:
            pop_idx = weights_idxes[i].popleft()
            if boxes[pop_idx] == 0:
                continue
            boxes[pop_idx] = 0
            break
    T += 1
    if sum(boxes) == 0:
        print(T)
        exit(0)
