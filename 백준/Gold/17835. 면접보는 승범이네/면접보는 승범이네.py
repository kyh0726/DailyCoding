import sys
import heapq
from collections import defaultdict
N, M, K = map(int, sys.stdin.readline().strip().split())

roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
graph = defaultdict(list)
INF = 1e10

for a,b,cost in roads:
    graph[b].append((a,cost))

goals = list(map(int, sys.stdin.readline().strip().split()))
distances = [INF] * (N+1)

def dijkstra():
    q = []
    for goal in goals:
        heapq.heappush(q, (0,goal))
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        
        if cur_cost > distances[cur_node]:
            continue
        
        distances[cur_node] = cur_cost
        
        for next_node, add_cost in graph[cur_node]:
            next_cost = cur_cost + add_cost

            if next_cost > distances[next_node]:
                continue
            
            heapq.heappush(q, (next_cost, next_node))



max_dist = 0
max_num = 0
    
dijkstra()

for i in range(1, N+1):
    if distances[i] == 0:
        continue
    if distances[i] > max_dist:
        max_dist = distances[i]
        max_num = i



print(max_num)

print(max_dist)

    