import sys

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


    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1, N+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index


    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        
        for i in range(N-1):
            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now] + j[1]

                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(C)
    answer = 0
    count = 0
    for i in range(1, N+1):
        if distance[i] != INF:
            count += 1
            answer = max(answer, distance[i])
    print(count, answer)




