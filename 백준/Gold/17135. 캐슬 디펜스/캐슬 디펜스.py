import sys, copy
from collections import deque
from itertools import combinations
import heapq
N, M, D = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
moves = [(0,1), (0,-1), (1,0),(-1,0)]
board.append([2] * M)


def bfs(positions, board):
    count = 0

    while True:
        kill_list = set()
        for c in positions:
            r = N
            kill_candidates = []
            q = deque()
            q.append((r,c))
            visited = [[False] * (M) for _ in range(N+1)]
            visited[r][c] = True
            while q:
                row, col = q.popleft()
                for dr, dc in moves:
                    next_r, next_c = row + dr, col + dc
                    if next_r > N or next_c >= M or next_r < 0 or next_c < 0:
                        continue
                    # 궁수의 사정거리 벗어난 경우
                    dist = abs(r- next_r) + abs(c-next_c)
                    if dist > D:
                        continue
                    if visited[next_r][next_c]:
                        continue

                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))
                    if board[next_r][next_c] == 1:
                        # 순서에 주의 ( 거리, col, row 순서), 가장 왼쪽부터 죽이기 때문
                        heapq.heappush(kill_candidates, (dist, next_c, next_r))
            
            if kill_candidates:
                dist, col, row = heapq.heappop(kill_candidates)
                kill_list.add((row,col))
        
        # 사살
        for row, col in kill_list:
            board[row][col] = 0
            count += 1


        # enemy 움직일 차례
        enemy_list = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    # 성 침략한 경우
                    if i == N-1:
                        board[i][j] = 0
                        continue
                    enemy_list.append((i+1,j))
                    board[i][j] = 0
        
        if not enemy_list:
            return count
        for r, c in enemy_list:
            board[r][c] = 1
        



# 궁수 배치될 수 있는 케이스들
archors = [i for i in range(M)]
combs = list(combinations(archors, 3))
max_count = 0
for comb in combs:
    copy_board = copy.deepcopy(board)
    max_count = max(max_count, bfs(comb, copy_board))
print(max_count)
        
                    
