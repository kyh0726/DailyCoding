import sys
from collections import deque
import heapq

N = int(sys.stdin.readline().strip())

hws = [0] * (N+1)
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

arr.sort(key = lambda x: (x[0]))
heap = []
for deadline, reward in arr:
    heapq.heappush(heap, reward)

    if len(heap) > deadline:
        heapq.heappop(heap)


print(sum(heap))