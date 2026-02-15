import sys
N = int(sys.stdin.readline().strip())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
counts = [[[0] * (3) for _ in range(N)] for _ in range(N)]

prev_dirs = {0:[0,2], 1:[1,2], 2:[1,2,0]}
moves = [(0,-1), (-1,0), (-1,-1)]

counts[0][1][0] = 1

def is_safe(row,col,dir):

    prev_row, prev_col = row + moves[dir][0], col + moves[dir][1]

    if prev_row < 0 or prev_col < 0:
        return False


    if dir == 2:
        for dr, dc in moves:
            if board[row + dr][col + dc] == 1:
                return False

    return True

def add_num(row, col, dir):
    count = 0
    prev_row, prev_col = row + moves[dir][0], col + moves[dir][1]

    for prev_dir in prev_dirs[dir]:
        count += counts[prev_row][prev_col][prev_dir]
    return count



for i in range(N):
    for j in range(N):
        for k in range(3):
            if board[i][j] == 1 or (not is_safe(i,j,k)):
                continue
            counts[i][j][k] += add_num(i,j,k)


print(sum(counts[N-1][N-1]))