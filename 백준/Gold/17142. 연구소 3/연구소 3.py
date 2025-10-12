import sys
from itertools import combinations
from collections import deque
import copy
N, M = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
MAX_NUM = 1e9

moves = [(1,0),(-1,0),(0,1),(0,-1)]
all_viruses = []
virus_idx = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            all_viruses.append((i,j))


for i in range(len(all_viruses)):
    virus_idx.append(i)


cases = list(combinations(virus_idx, M))
result = MAX_NUM
for case in cases:
    copy_board = copy.deepcopy(board)
    # 벽은 -1, 임시 바이러스 위치는 -2, 그냥 길은 1e9로 두자


    q = deque()


    for i in range(N):
        for j in range(N):
            if copy_board[i][j] == 0:
                copy_board[i][j] = MAX_NUM
            elif copy_board[i][j] == 1:
                copy_board[i][j] = -1
            elif copy_board[i][j] == 2:
                copy_board[i][j] = MAX_NUM
    for idx in case:
        r,c = all_viruses[idx]
        q.append((r,c,0))
        copy_board[r][c] = 0

    while q:
        row, col, count = q.popleft()

        for dr, dc in moves:
            next_r, next_c, next_count = row + dr, col + dc, count + 1
            if not (0 <= next_r < N) or not (0 <= next_c < N):
                continue
            if next_count >= copy_board[next_r][next_c]:
                continue
            
            copy_board[next_r][next_c] = next_count
            q.append((next_r,next_c,next_count))
    
    max_num = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                continue
            max_num = max(max_num, copy_board[i][j])
    
    result = min(max_num, result)


if result == MAX_NUM:
    print(-1)
else:
    print(result)    
    


