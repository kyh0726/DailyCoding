import sys
N = 19

line = [0] * 21
board = []
board.append(line)
for i in range(19):
    board.append([0] + list(map(int, sys.stdin.readline().strip().split())) + [0])
board.append(line)

moves = [(0,1), (1,1), (1,0), (-1,1)]


def is_winner(r, c):
    cur_color = board[r][c]
    
    for dr, dc in moves:
        isFail = False
        for i in range(1,5):
            next_r, next_c = r + dr * i, c + dc * i

            if board[next_r][next_c] != cur_color:
                isFail = True
                break

        if (isFail):
            continue

        # 다섯 개의 알이 다 통과한 경우 좌우값 검증
        prev_r, prev_c = r - dr, c - dc
        next_r, next_c = r + dr * 5, c + dc * 5

        if board[prev_r][prev_c] != cur_color and board[next_r][next_c] != cur_color:
            return True
    return False




for i in range(1,20):
    for j in range(1,20):
        if board[i][j] != 0 and is_winner(i,j):
            print(board[i][j])
            print(i, j)
            exit(0)
print(0)

