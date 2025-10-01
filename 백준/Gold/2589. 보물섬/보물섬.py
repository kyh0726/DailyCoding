import sys
from collections import deque
max_count = 0
R, C = map(int, sys.stdin.readline().strip().split())
moves = [(1,0), (-1,0), (0,1), (0,-1)]
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]


def bfs(row, col):
    q = deque()
    global max_count
    q.append((row, col, 0))
    visited = [[False] * C for _ in range(R)]
    visited[row][col] = True
    while q:
        pop_row, pop_col, count = q.popleft()
        max_count = max(count, max_count)

        for dr, dc in moves:
            next_r, next_c = pop_row + dr, pop_col + dc
            if next_r >= R or next_c >= C or next_r < 0 or next_c < 0 or visited[next_r][next_c]:
                continue
            if maps[next_r][next_c] == "W":
                continue
            visited[next_r][next_c] = True
            q.append((next_r, next_c, count + 1)) 


for i in range(R):
    for j in range(C):
        if maps[i][j] == "L":
            bfs(i,j)

print(max_count)
