import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_distance = 0
moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
def bfs(row, col):
  global max_distance
  q = deque()
  q.append((row, col, 0))
  visited = [[False] * M for _ in range(N)]
  distance = 25000
  while q:
    r, c, count = q.popleft()
    if visited[r][c]:
      continue
    visited[r][c] = True
    if board[r][c]:
      distance= min(count, distance)

    for dr, dc in moves:
      next_r, next_c = r + dr, c + dc
      if next_r >= N or next_c >= M or next_r < 0 or next_c < 0:
        continue
      if visited[next_r][next_c]:
        continue
      q.append((next_r, next_c, count + 1))

  max_distance = max(max_distance, distance)
          



for i in range(N):
  for j in range(M):
    if board[i][j] == 0:
      bfs(i,j)


print(max_distance)