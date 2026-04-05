import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

pattern_board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]

patterns = []

moves = [(0,1), (0,-1), (1,0), (-1,0)]

for row in range(5):
    for col in range(5):
        if pattern_board[row][col] == 1 and (row,col) != (2,2):
            patterns.append((row - 2, col - 2))


INF = 10**15

count_board = [[[[INF] * 2 for _ in range (K+1)] for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0,0,0,0))
count_board[0][0][0][0]= 0

while q:
    row, col, pattern_count, hasVisited = q.popleft()
    count = count_board[row][col][pattern_count][hasVisited]

    if (row,col,hasVisited) == (N-1,M-1,1):
        print(count)
        exit(0)

    for dr, dc in moves:
        next_r, next_c = row + dr, col + dc

        if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
            continue

        if board[next_r][next_c] == 1:
            continue
        
        
        if board[next_r][next_c] == 2:
            if count_board[next_r][next_c][pattern_count][1] != INF:
                continue
            count_board[next_r][next_c][pattern_count][1] = count + 1
            q.append((next_r,next_c,pattern_count, 1))
        else:
            if count_board[next_r][next_c][pattern_count][hasVisited] != INF:
                continue
            count_board[next_r][next_c][pattern_count][hasVisited] = count + 1
            q.append((next_r,next_c,pattern_count, hasVisited))

    

    if pattern_count == K:
        continue

    for dr, dc in patterns:
        next_r, next_c = row + dr, col + dc

        if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
            continue

        if board[next_r][next_c] == 1:
            continue


        if board[next_r][next_c] == 2:
            if count_board[next_r][next_c][pattern_count+1][1] != INF:
                continue
            count_board[next_r][next_c][pattern_count+1][1] = count + 1
            q.append((next_r,next_c,pattern_count+1, 1))
        else:
            if count_board[next_r][next_c][pattern_count+1][hasVisited] != INF:
                continue
            count_board[next_r][next_c][pattern_count+1][hasVisited] = count + 1
            q.append((next_r,next_c,pattern_count+1, hasVisited))


min_val = INF

for i in range(K+1):
    min_val = min(min_val,count_board[N-1][M-1][i][1])


if min_val == INF:
    print(-1)
else:
    print(min_val)
