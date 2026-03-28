import sys
import heapq
from collections import defaultdict


N,P,K = map(int, sys.stdin.readline().strip().split())

cables = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(P)]
graph = defaultdict(list)
for a,b,cost in cables:
    graph[a].append((b,cost))
    graph[b].append((a,cost))

def dijkstra(cost):
    distances = [1e10] * (N+1)
    distances[1] = 0

    pq = []
    heapq.heappush(pq, [0,1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost:
            continue

        for next_node, next_cost in graph[cur_node]:
            if next_cost > cost:
                if distances[next_node] > cur_cost + 1:
                    distances[next_node] = cur_cost + 1
                    heapq.heappush(pq, [cur_cost + 1, next_node])

            else:
                if distances[next_node] > cur_cost:
                    distances[next_node] = cur_cost
                    heapq.heappush(pq, [cur_cost, next_node])

    return distances[N]


left = 0
right = 1e6
answer = 1e6
while left <= right:
    middle = (left + right) // 2

    result = dijkstra(middle)

    if result == 1e10:
        print(-1)
        exit(0)

    if result <= K:
        answer = middle
        right = middle - 1
    else:
        left = middle + 1

    

print(int(answer))