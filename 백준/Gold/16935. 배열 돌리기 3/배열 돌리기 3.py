import sys

N, M, R = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def up_down_reverse(board):
    row_len = len(board)
    col_len = len(board[0])
    for i in range(row_len//2):
        for j in range(col_len):
            board[i][j], board[row_len-1-i][j] = board[row_len-1-i][j], board[i][j]
    return board

def left_right_reverse(board):
    row_len = len(board)
    col_len = len(board[0])

    for j in range(col_len//2):
        for i in range(row_len):
            board[i][j], board[i][col_len-1-j] = board[i][col_len-1-j], board[i][j]
    return board

# row = col, row -> max_col - col
def right_rotate(board):
    row_len = len(board)
    col_len = len(board[0])
    temp = [[0] * row_len for _ in range(col_len)]

    for i in range(col_len):
        for j in range(row_len):
            temp[i][j] = board[row_len-1-j][i]

    return temp

def left_rotate(board):
    row_len = len(board)
    col_len = len(board[0])
    temp = [[0] * row_len for _ in range(col_len)]

    for i in range(col_len):
        for j in range(row_len):
            temp[i][j] = board[j][col_len - 1 -i]


    return temp

def find_portion(r, c, board):
    half_row_len = len(board) // 2
    half_col_len = len(board[0]) // 2

    if r < half_row_len and c < half_col_len:
        return 1
    if r < half_row_len and c >= half_col_len:
        return 2
    if r >= half_row_len and c >= half_col_len:
        return 3
    if r >= half_row_len and c < half_col_len:
        return 4


def five_fun(board):
    half_row_len = len(board) // 2
    half_col_len = len(board[0]) // 2

    temp = [[0] * half_col_len * 2 for _ in range(half_row_len * 2)]

    portion_mapper = {1:[1,0], 2:[0,-1], 3:[-1,0], 4:[0,1]}

    for i in range(half_row_len*2):
        for j in range(half_col_len*2):
            portion = find_portion(i,j, board)
            dr, dc = portion_mapper[portion]
            temp[i][j] = board[i + dr * half_row_len][j + dc * half_col_len]
    return temp

def six_fun(board):
    half_row_len = len(board) // 2
    half_col_len = len(board[0]) // 2

    temp = [[0] * half_col_len * 2 for _ in range(half_row_len * 2)]

    portion_mapper = {1:[0,1], 2:[1,0], 3:[0,-1], 4:[-1,0]}

    for i in range(half_row_len*2):
        for j in range(half_col_len*2):
            portion = find_portion(i,j, board)
            dr, dc = portion_mapper[portion]
            temp[i][j] = board[i + dr * half_row_len][j + dc * half_col_len]
    return temp

func_mapper = {1:up_down_reverse, 2:left_right_reverse, 3:right_rotate, 4: left_rotate, 5: five_fun, 6: six_fun}


commands = list(map(int, sys.stdin.readline().strip().split()))


for command in commands:
    board = func_mapper[command](board)

for row in board:
    for val in row:
        print(val, end=" ")
    print()