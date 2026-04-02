import sys

N,M,S,T = map(int, sys.stdin.readline().strip().split())
INF = 10**18
roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

graph = [[INF] * (N+1) for _ in range(N+1)]

for prev, post, cost in roads:
    graph[prev][post] = min(graph[prev][post], cost)
for i in range(1, N+1):
    graph[i][i] = 0

Q = int(sys.stdin.readline().strip())

cases = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(Q)]


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            
for case in cases:
    a1,b1,c1,a2,b2,c2 = case
    candidates = [graph[S][a1] + c1 + graph[b1][T],
                  graph[S][a2] + c2 + graph[b2][T],
                  graph[S][a1] + c1 + graph[b1][a2] + c2 + graph[b2][T],
                  graph[S][a2] + c1 + graph[b2][a1] + c2 + graph[b1][T],
                  graph[S][T]
                ]
    

    result = min(candidates)
    if result == INF:
        print(-1)
        continue
    print(result)
