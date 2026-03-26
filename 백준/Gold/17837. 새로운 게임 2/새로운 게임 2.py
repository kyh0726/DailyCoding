import sys
from collections import defaultdict
N, K = map(int, sys.stdin.readline().strip().split())


board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
moves = [(0,1),(0,-1),(-1,0),(1,0)]
horses = defaultdict(list)

WHITE = 0
RED = 1
BLUE = 2

for i in range(K):
    r,c,dir = map(int, sys.stdin.readline().strip().split())
    horses[(r-1,c-1)].append([i, dir - 1])



def find_index(i):
    for r in range(N):
        for c in range(N):
            for idx in range(len(horses[(r,c)])):
                if horses[(r,c)][idx][0] == i:
                    return (r,c,idx)


def change_dir(dir):
    if dir == 0:
        return 1
    if dir == 1:
        return 0
    if dir == 2:
        return 3
    if dir == 3:
        return 2

def move(r,c,idx,isRetry):
    global t

    dir = horses[(r,c)][idx][1]

    dr, dc = moves[dir]

    next_r, next_c = r + dr, c + dc

    if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
        if isRetry:
            return False
        horses[(r,c)][idx][1] = change_dir(dir)
        return False
    
    if board[next_r][next_c] == BLUE:
        if isRetry:
            return False
        horses[(r,c)][idx][1] = change_dir(dir)
        return False



    if board[next_r][next_c] == WHITE:
        left_horses = horses[(r,c)][:idx]
        move_horses = horses[(r,c)][idx:]

        horses[(r,c)] = left_horses
        horses[(next_r,next_c)].extend(move_horses)
        
    if board[next_r][next_c] == RED:
        left_horses = horses[(r,c)][:idx]
        move_horses = horses[(r,c)][idx:]

        horses[(r,c)] = left_horses
        horses[(next_r,next_c)].extend(reversed(move_horses))
    if len(horses[(next_r,next_c)]) >= 4:
        print(t)
        exit(0)

    return True


t = 0




while t <= 1000:
    t += 1

    


    for i in range(K):
        r,c,idx = find_index(i)


        result = move(r,c,idx,False)
        if not result:
            move(r,c,idx,True)

        


print(-1)
