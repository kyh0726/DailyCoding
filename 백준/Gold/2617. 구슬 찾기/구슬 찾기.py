import sys


N, M = map(int, sys.stdin.readline().strip().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = 1
    graph[b][a] = -1

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if graph[j][i] * graph[i][k] > 0:
                graph[j][k] = graph[j][i]


result = 0
for row in graph:
    threshold = [0,0]
    for val in row:
        if val == -1:
            threshold[0] += 1
        if val == 1:
            threshold[1] += 1
    
    if threshold[0] > N // 2 or threshold[1] > N // 2:
        result += 1

print(result)