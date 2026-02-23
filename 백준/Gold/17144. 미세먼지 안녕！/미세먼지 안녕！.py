# 10:18 시작
import sys
from collections import defaultdict

R,C,T = map(int, sys.stdin.readline().strip().split())

upper_moves = [(0,1), (-1,0), (0,-1), (1,0)]
lower_moves = [(0,1), (1,0), (0,-1), (-1,0)]

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]


def spread(r,c, temp):
    count = 0
    for dr, dc in upper_moves:
        next_r, next_c = r + dr, c + dc

        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            continue
        if board[next_r][next_c] == -1:
            continue
    
        temp[(next_r,next_c)] += (board[r][c]) // 5
        count += 1

    temp[(r,c)] += board[r][c] - ((board[r][c]) // 5) * count
    

def circulate(r,c,type):
    moves = []
    if type == "upper":
        moves = upper_moves
    else:
        moves = lower_moves

    cur_dir = 0
    cur_r, cur_c = r,c
    prev_val = 0
    while True:
        dr, dc = moves[cur_dir]
        next_r, next_c = cur_r + dr, cur_c + dc

        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            cur_dir = (cur_dir + 1)
            dr, dc = moves[cur_dir]
            next_r, next_c = cur_r + dr, cur_c + dc
        
        if board[next_r][next_c] == -1:
            break

        # 값들 교환
        new_val = board[next_r][next_c]
        board[next_r][next_c] = prev_val
        prev_val = new_val
        cur_r, cur_c = next_r, next_c



air_conditioner_pos = []

for i in range(R):
    if len(air_conditioner_pos) > 0:
        break
    for j in range(C):
        if board[i][j] == -1:
            air_conditioner_pos = [i,j]
            break
    



for _ in range(T):
    temp = defaultdict(int)
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                spread(i,j,temp)
            
            if board[i][j] == -1:
                temp[(i,j)] = -1


    for i in range(R):
        for j in range(C):
            board[i][j] = temp[(i,j)]
    

    circulate(air_conditioner_pos[0], air_conditioner_pos[1], "upper")
    circulate(air_conditioner_pos[0]+1, air_conditioner_pos[1], "lower")


result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == -1: 
            continue
        result += board[i][j]

print(result)