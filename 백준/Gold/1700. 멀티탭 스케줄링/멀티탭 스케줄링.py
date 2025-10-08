import sys
from collections import defaultdict
import heapq
N, K = map(int, sys.stdin.readline().strip().split())

arr = list(map(lambda x: [int(x), 1000], sys.stdin.readline().strip().split()))
using_time = defaultdict(int)
q = []


for i in range(K-1, -1, -1):
    num = arr[i][0]
    if using_time[num]:
        idx = using_time[num]
        arr[i][1] = idx
        using_time[num] = i
    else:
        using_time[num] = i

count = 0

for val, next_idx in arr:
    isSame = False
    for i in range(len(q)):
        remaining_idx, remaining_val = q[i]
        if remaining_val == val:
            q.remove((remaining_idx,remaining_val))
            heapq.heappush(q, (-next_idx, val)) 
            isSame = True
    if isSame:
        continue

    if q and len(q) == N:
        idx, last_val = heapq.heappop(q)
        # swapping 발생
        heapq.heappush(q, (-next_idx, val))
        count += 1
        continue
    heapq.heappush(q, (-next_idx, val))

print(count)
