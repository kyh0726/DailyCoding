import sys
from collections import deque

R, C = map(int, sys.stdin.readline().strip().split())

maps = [list((sys.stdin.readline().strip())) for _ in range(R)]
start = []
end = []
stones = []
water = []
moves = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            start = [i,j]
        if maps[i][j] == 'D':
            end = [i,j]
        if maps[i][j] == 'X':
            stones.append((i,j))
        if maps[i][j] == '*':
            water.append((i,j))


q = deque()
q.append((start[0], start[1], 0))
cur_time = 0
visited[start[0]][start[1]] = True
isEnd = False
while q:
    pop_row, pop_col, time = q.popleft()
    if cur_time == time:
        add_water_set = set()
        for row, col in water:
            for dr, dc in moves:
                next_row, next_col = row + dr, col + dc
                if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                    continue
                if maps[next_row][next_col] == 'X':
                    continue
                if maps[next_row][next_col] == '*':
                    continue
                if maps[next_row][next_col] == 'D':
                    continue

                if maps[next_row][next_col] == '.':
                    add_water_set.add((next_row, next_col))
                
        for row, col in list(add_water_set):
            water.append((row, col))
        cur_time += 1

                    
        

    for dr, dc in moves:
        next_row, next_col = pop_row + dr, pop_col + dc
        if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
            continue
        if maps[next_row][next_col] == 'X':
            continue
        if maps[next_row][next_col] == '*':
            continue
        if (next_row, next_col) in water:
            continue
        if maps[next_row][next_col] == '.' and not visited[next_row][next_col]:
            q.append((next_row, next_col, time + 1))
            visited[next_row][next_col] = True
        if maps[next_row][next_col] == 'D':
            isEnd = True
            print(time + 1)
            break
    if isEnd:
        break


if not isEnd:
    print('KAKTUS')

