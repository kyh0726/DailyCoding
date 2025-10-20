import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

moves = [(0,-1),(-1,0),(-1,-1)]

for i in range(1,N):
    for j in range(1,M):
        if board[i][j] == 0:
            continue
        min_val = 1e9
        for dr, dc in moves:
            next_r, next_c = i + dr, j + dc
            min_val = min(min_val, board[next_r][next_c])

        board[i][j] = min_val + 1

print(max(max(row) for row in board)**2)