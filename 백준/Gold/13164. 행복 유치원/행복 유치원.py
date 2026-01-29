import sys
import heapq

N, K = map(int, sys.stdin.readline().strip().split())

kids = list(map(int, sys.stdin.readline().strip().split()))
result = 0
diffs = []

for i in range(1,N):
    heapq.heappush(diffs, kids[i] - kids[i-1])

for i in range(N-K):
    result += heapq.heappop(diffs)

print(result)