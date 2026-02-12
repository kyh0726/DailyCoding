import sys
from collections import deque, defaultdict

A, B, C = map(int, sys.stdin.readline().strip().split())



q = deque()
combs = [(0,1,2), (1,2,0), (0,2,1)]
visited = defaultdict(int)
result = False
q.append((A,B,C))
while q:
    vals = q.popleft()

    if len(set(vals)) == 1:
        result = True
        break

    if visited[tuple(sorted(vals))]:
        continue

    visited[tuple(sorted(vals))] = True

    for idx1, idx2, preserved_idx in combs:
        val1 = vals[idx1]
        val2 = vals[idx2]
        preserved_val = vals[preserved_idx]

        if val1 == val2:
            continue
        
        if val1 < val2:
            q.append((val1 + val1, val2 - val1, preserved_val))
        else:
            q.append((val1 - val2, val2 + val2, preserved_val))


if result:
    print(1)
else:
    print(0)