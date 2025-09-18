import sys
import heapq
K = int(sys.stdin.readline().strip())
INF = int(1e9)


for i in range(K):
    N, D, C = map(int, sys.stdin.readline().strip().split())
    graph = [[] for i in range(N+1)]
    
    start = C
    distance = [INF] * (N+1)
    visited = [False] * (N+1)


    for j in range(D):
        a, b, s = map(int, sys.stdin.readline().strip().split())
        graph[b].append((a,s))


    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            cur_cost, now = heapq.heappop(q)
            if distance[now] < cur_cost:
                continue

            for next_node, add_cost in graph[now]:
                cost = cur_cost + add_cost
                
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))


    dijkstra(C)
    answer = 0
    count = 0
    for i in range(1, N+1):
        if distance[i] != INF:
            count += 1
            answer = max(answer, distance[i])
    print(count, answer)




