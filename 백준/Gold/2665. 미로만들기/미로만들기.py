import sys
import copy
import heapq
from collections import deque


N = int(sys.stdin.readline().strip())

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] = 1
        else:
            board[i][j] = 0

moves = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [[0] * N for _ in range(N)]
def bfs():
    q = deque()

    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            next_r, next_c = r + dr, c + dc

            if not (0 <= next_r < N) or not (0 <= next_c < N):
                continue
            if visited[next_r][next_c] == 0:
                visited[next_r][next_c] = visited[r][c] + board[next_r][next_c]
                q.append((next_r,next_c))
                continue
            if visited[r][c] + board[next_r][next_c] >= visited[next_r][next_c]:
                continue

            
            visited[next_r][next_c] = visited[r][c] + board[next_r][next_c]
            q.append((next_r, next_c))


bfs()

print(visited[N-1][N-1] - 1)








