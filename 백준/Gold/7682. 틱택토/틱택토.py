import sys
from collections import deque, defaultdict

import copy


result_dict = defaultdict(int)

def make_case():
    q = deque()

    start_board = []
    for i in range(9):
        start_board.append('.')
    
    q.append((start_board,0))

    while q:
        cur_board, turn = q.popleft()

        cur_color = "X" if turn % 2 == 0 else "O"
        
        if check_is_end(cur_board) or turn == 9:
            result_dict[tuple(cur_board)] = 1
            continue


        for i in range(9):
            if cur_board[i] == "X" or cur_board[i] == "O":
                continue
            new_board = copy.deepcopy(cur_board)
            new_board[i] = cur_color
            q.append((new_board, turn + 1))



def check_is_end(board):

    for i in range(3):
        if board[3*i] == board[3*i+1] == board[3*i+2] and board[3*i] != ".":
            return True
    
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ".":
            return True
    
    if (board[0] == board[4] == board[8] and board[0] != ".") or (board[2] == board[4] == board[6] and board[2] != "."):
        return True
    return False

make_case()

while True:
    board_string = sys.stdin.readline().strip()

    if board_string == "end":
        exit(0)

    board = list(board_string)

    if result_dict[tuple(board)]:
        print("valid")
        continue
    print("invalid")