import sys
import copy
from itertools import combinations
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
virus_candidates = []
moves = [(0,1), (0,-1), (1,0), (-1,0)]

empty_num = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            virus_candidates.append((r,c))
            empty_num += 1

        if board[r][c] == 0:
            empty_num += 1

min_time = 1e10

cases = list(combinations(virus_candidates, M))



for start_viruses in cases:
    q = deque()
    visited = [[False] * N for _ in range(N)]

    infect_counter = 0

    for r, c in start_viruses:
        q.append((r, c, 0))
        visited[r][c] = True

    
    while q:
        row, col, count = q.popleft()
        infect_counter += 1
        if infect_counter == empty_num:
            min_time = min(min_time, count)

        for dr, dc in moves:
            next_r, next_c = row + dr , col + dc

            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
                continue
            if visited[next_r][next_c]:
                continue
            if board[next_r][next_c] == 1:
                continue
            
            
            q.append((next_r,next_c, count + 1))
            visited[next_r][next_c] = True


    

    




if min_time == 1e10:
    print(-1)
else:
    print(min_time)