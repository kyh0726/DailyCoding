import sys
import copy

max_count = 0
arr = [list(map(int, sys.stdin.readline().strip().split()))for i in range(4)]
dirs = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
# board에서 상어가 차지하는 곳: (-1,-1), 아무것도 없는 곳: (0,0)
board = []
for i in range(4):
    rows = []
    for j in range(4):
        rows.append([arr[i][2*j], arr[i][2*j+1]-1])
    board.append(rows)



def dfs(start_row, start_col, count, board):
    add_count, shark_dir= board[start_row][start_col]
    count += add_count
    board[start_row][start_col] = [0,0]

    global max_count
    max_count = max(max_count, count)


    for num in range(1,17):
        r, c = -1,-1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == num:
                    r,c = i,j
                    break
        
        if (r,c) == (-1,-1):
            continue

        dir = board[r][c][1]

        for i in range(8):
            next_dir = (dir + i) % 8
            dr,dc = dirs[next_dir]
            next_r, next_c = r + dr, c + dc
            if next_r < 0 or next_c < 0 or next_r >=4 or next_c >=4 or (next_r == start_row and next_c == start_col):
                continue
            
            # switching
            board[r][c][1] = next_dir
            board[r][c], board[next_r][next_c] = board[next_r][next_c], board[r][c]
            break
    # 이동 다 마친 후에
    dr, dc = dirs[shark_dir]
    for i in range(1,5):
        next_r, next_c = start_row + dr * i, start_col + dc * i
        if next_r >= 4 or next_c >= 4 or next_r < 0 or next_c < 0 or board[next_r][next_c][0] == 0:
            continue
        dfs(next_r,next_c,count,copy.deepcopy(board))


dfs(0,0,0,board)


print(max_count)