import sys
from collections import deque
board = []
moves = [(1,0),(-1,0),(0,1),(0,-1)]
C = 6
R = 12

def find_near_blocks(r,c,color):
    q = deque()
    near_blocks = []
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True
    q.append((r,c))
    
    while q:
        row, col = q.popleft()
        near_blocks.append((row,col))
        for dr,dc in moves:
            next_r, next_c = row + dr, col + dc
            if next_r >= R or next_c >= C or next_r < 0 or next_c < 0:
                continue
            if visited[next_r][next_c]:
                continue
            if color != board[next_r][next_c]:
                continue
            visited[next_r][next_c] = True
            q.append((next_r, next_c))
    return near_blocks

def go_down_blocks():
    for j in range(6):
        for i in range(11,0,-1):
            if board[i][j] != ".":
                continue
            change_idx = i-1
            while change_idx >= 0:
                if board[change_idx][j] != '.':
                    break
                change_idx -= 1
            # 바꿀 게 없는 경우
            if change_idx == -1:
                break            
            else:
                board[i][j], board[change_idx][j] = board[change_idx][j], board[i][j]




for i in range(12):
    board.append(list(sys.stdin.readline().strip()))
T = 0
while True:
    will_be_deleted = set()
    temp_visited = set()
    for i in range(R):
        for j in range(C):
            if board[i][j] == "." or (i,j) in will_be_deleted or (i,j) in temp_visited:
                continue
            else:
                target_color = board[i][j]
                arr = find_near_blocks(i,j,target_color)
                if len(arr) < 4:
                    for r,c in arr:
                        temp_visited.add((r,c))
                else:
                    for r,c in arr:
                        will_be_deleted.add((r,c))
    
    if not will_be_deleted:
        break
    
    for r,c in will_be_deleted:
        board[r][c] = '.'
    

    go_down_blocks()
    

    T += 1

print(T)



