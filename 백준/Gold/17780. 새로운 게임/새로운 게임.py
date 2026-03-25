import sys
from collections import deque, defaultdict

N, K = map(int,sys.stdin.readline().strip().split())

WHITE = 0
RED = 1
BLUE = 2


board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

directions = [(0,1), (0,-1), (-1,0), (1,0)]
positions = defaultdict(deque)

for idx in range(K):
    R,C,dir = map(int, sys.stdin.readline().strip().split())
    positions[(R-1,C-1)].append((idx, dir-1))

t = 0

def find_cur_idx(cur_idx):
    for r in range(N):
        for c in range(N):
            if len(positions[(r,c)]) > 0 and positions[(r,c)][0][0] == cur_idx:
                return (r,c)
    return (-1,-1)


def move(cur_pos):
    r, c = cur_pos

    position_info = positions[(r,c)]

    dr, dc = directions[position_info[0][1]]

    next_r, next_c = r + dr, c + dc

    if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
        idx, cur_dir = position_info[0]
        next_dir = change_direction(cur_dir)
        position_info[0] = (idx, next_dir)
        positions[(r,c)] = position_info
        return False
    
    if board[next_r][next_c] == BLUE:
        idx, cur_dir = position_info[0]
        next_dir = change_direction(cur_dir)
        position_info[0] = (idx, next_dir)
        positions[(r,c)] = position_info
        return False
    
    if board[next_r][next_c] == WHITE:
        positions[(next_r,next_c)].extend(position_info)
        positions[(r,c)] = deque()
        return True
    
    if board[next_r][next_c] == RED:
        position_info.reverse()
        positions[(next_r,next_c)].extend(position_info)
        positions[(r,c)] = deque()
        return True


def change_direction(cur_dir):
    if cur_dir == 0:
        return 1
    if cur_dir == 1:
        return 0
    if cur_dir == 2:
        return 3
    if cur_dir == 3:
        return 2

def is_success():
    for r in range(N):
        for c in range(N):
            if len(positions[(r,c)]) >= 4:
                return True
            
    
    return False






while t <= 1000:
    for cur_idx in range(K):

        cur_pos = find_cur_idx(cur_idx)
        if cur_pos == (-1,-1):
            continue
        

        result = move(cur_pos)
        if not result:
            move(cur_pos)
    
    t += 1

    if is_success():
        print(t)
        exit(0)


print(-1)
    
