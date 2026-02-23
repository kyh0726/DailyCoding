# 10:51 시작

import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline().strip())
buliding_idx = defaultdict(list)
building_count = defaultdict(int)
buildings = list(map(int, sys.stdin.readline().strip().split()))

results = [-1] * N
reverse_results = [-1] * N
stack = []
reverse_stack = []

for idx, val in enumerate(buildings):

    while stack and buildings[stack[-1]] <= val:
        pop_idx = stack.pop()
    building_count[idx] += len(stack)

    if stack:
        heapq.heappush(buliding_idx[idx], (abs(idx - stack[-1]), stack[-1]))

    stack.append(idx)



for idx in range(N-1,-1,-1):
    
    while reverse_stack and buildings[reverse_stack[-1]] <= buildings[idx]:
        pop_idx = reverse_stack.pop()
    building_count[idx] += len(reverse_stack)

    if reverse_stack:
        heapq.heappush(buliding_idx[idx], (abs(idx - reverse_stack[-1]), reverse_stack[-1]))

    reverse_stack.append(idx)




for i in range(N):
    if building_count[i] == 0:
        print(0)
    else:
        print(building_count[i], heapq.heappop(buliding_idx[i])[1] + 1)