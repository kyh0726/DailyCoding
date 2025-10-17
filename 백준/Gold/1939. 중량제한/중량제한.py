import sys
from collections import defaultdict, deque
import heapq

INF = 1e10
N, M = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)
caps = [-1] * (N+1)
for i in range(M):
    A, B, C = map(int,sys.stdin.readline().strip().split())
    graph[A].append((B,C))
    graph[B].append((A,C))


start, end = map(int, sys.stdin.readline().strip().split())


q = []
heapq.heappush(q, (-INF, start))
caps[start] = -INF

while q:
    cap, node = heapq.heappop(q)
    cap *= -1
    if caps[node] > cap:
        continue

    caps[node] = cap
    if node == end:
        break
    for next_node, next_cap in graph[node]:
        next_cap = min(next_cap, cap)
        if next_cap > caps[next_node]:
            heapq.heappush(q, (-next_cap, next_node))



    
    

print(caps[end])