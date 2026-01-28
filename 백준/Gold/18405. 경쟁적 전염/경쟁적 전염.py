import sys
import heapq

N, K = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
moves = [(0,1), (0,-1), (1,0), (-1,0)]
viruses = []
S, X, Y = map(int, sys.stdin.readline().strip().split())


for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            heapq.heappush(viruses, (0, board[i][j], i, j))


while viruses:
    count, v_num, r, c = heapq.heappop(viruses)

    for dr, dc in moves:
        next_r, next_c = r + dr, c + dc

        if next_r >= N or next_c >= N or next_r < 0 or next_c < 0:
            continue
        if board[next_r][next_c] != 0:
            continue
        if count == S:
            continue

        board[next_r][next_c] = v_num
        heapq.heappush(viruses, (count + 1, v_num, next_r, next_c))


    

print(board[X-1][Y-1])