import sys
from collections import deque
import copy

N, K = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
INF = 1e10
distances = [INF] * N


start = K

q = deque()
q.append((start, 0, set([start])))
result = 1e10

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

while q:

    cur_node, cur_dist, visited = q.popleft()
    if len(visited) == N:
        result = min(result, int(cur_dist))
        continue

    for next_node in range(N):
        if next_node in visited:
            continue
        visited_copy = copy.deepcopy(visited)
        visited_copy.add(next_node)
        add_dist = board[cur_node][next_node]
        next_dist = add_dist + cur_dist
        q.append((next_node, next_dist, visited_copy))


print(result)
