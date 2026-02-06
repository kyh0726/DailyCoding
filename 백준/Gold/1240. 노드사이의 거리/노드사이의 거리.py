import sys
import heapq
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())

nodes = defaultdict(list)
q = []

for i in range(N-1):
    a,b,distance = map(int, sys.stdin.readline().strip().split())

    nodes[a].append((b,distance))
    nodes[b].append((a,distance))

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distances = [1e10] * (N+1)

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if cur_node == end:
            return cur_cost

        # 더 나은 경로가 이미 탐색된 경우
        if cur_cost > distances[cur_node]:
            continue


        # 현재 노드와 연결된 노드 탐색
        for next_node, add_cost in nodes[cur_node]:
            next_cost = cur_cost + add_cost
            if next_cost < distances[next_node]:
                heapq.heappush(q, (next_cost, next_node))
                distances[next_node] = next_cost




for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())

    print(dijkstra(a,b))





            
            


