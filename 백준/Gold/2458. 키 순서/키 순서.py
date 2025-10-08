import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True



answer = 0

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] or graph[j][i]:
            count += 1

    
    if count == N-1:
        answer += 1


print(answer)