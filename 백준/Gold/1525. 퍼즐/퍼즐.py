import sys
from collections import deque
import copy
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]


empty_pos = [-1,-1]
visited = set()
moves = [(0,1), (0,-1), (1,0), (-1,0)]
def check_is_clear(board):
    count = 1

    for i in range(3):
        for j in range(3):
            if board[i][j] != count:
                return -1
            count = (count + 1)%9
    return 1
    

def put_board_into_memo(board):
    temp = []
    for row in board:
        temp.extend(row)

    tuple_temp = tuple(temp)
    if tuple_temp in visited:
        return False
    visited.add(tuple_temp)
    return True


def bfs(board, row, col):
    q = deque()
    q.append((0, board, row, col))
    put_board_into_memo(board)

    while q:
        count, board, r, c = q.popleft()

        if check_is_clear(board) == 1:
            return count
        for dr, dc in moves:
            next_r, next_c = r + dr, c + dc
            
            if next_r < 0 or next_c < 0 or next_r >= 3 or next_c >= 3:
                continue
            
            copy_board = copy.deepcopy(board)
            
            copy_board[next_r][next_c], copy_board[r][c] = copy_board[r][c], copy_board[next_r][next_c]

            if not put_board_into_memo(copy_board):
                continue
            q.append((count + 1, copy_board, next_r, next_c))
            
    return -1

    

for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            empty_pos = [i,j]


result = bfs(board, empty_pos[0], empty_pos[1])
            
print(result)