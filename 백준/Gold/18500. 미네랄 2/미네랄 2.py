import sys
from collections import deque
import copy
R, C = map(int, sys.stdin.readline().strip().split())

caves = [list(sys.stdin.readline().strip()) for _ in range(R)]

caves.reverse()

moves = [(0,1),(1,0),(-1,0),(0,-1)]

N = int(sys.stdin.readline().strip())

heights = list(map(int, sys.stdin.readline().strip().split()))

def destroy_mineral(direction, height):
    
    start_col = 0 if direction == 1 else C-1
    end_col = C if direction == 1 else -1
    
    for col in range(start_col, end_col, direction):
        if caves[height][col] == 'x':
            caves[height][col] = '.'
            return (height, col)
    return (-1,-1)


def fall_mineral(mineral_position):
    minerals = find_near_minerals(mineral_position)

    start_minerals = set(copy.deepcopy(minerals))

    isSame = True

    while True:
        isSuccess = True
        next_minerals = []

        for row, col in minerals:
            next_r, next_c = row - 1, col

            if not (0 <= next_r < R) or not (0 <= next_c < C):
                isSuccess = False
                break
            if (next_r, next_c) not in start_minerals and caves[next_r][next_c] == "x":
                isSuccess = False
                break

            next_minerals.append((next_r,next_c))

        if not isSuccess:
            break
        else:
            isSame = False
            minerals = next_minerals

    if not isSame:
        for row, col in start_minerals:
            caves[row][col] = '.'


        for row, col in minerals:
            caves[row][col] = 'x'





def find_near_minerals(mineral_position):

    result = [mineral_position]
    q = deque()
    q.append(mineral_position)
    visited = [[False]*C for _ in range(R)]
    visited[mineral_position[0]][mineral_position[1]] = True
    while q:
        row, col = q.popleft()

        for dr, dc in moves:
            next_r, next_c = row + dr, col + dc

            if not (0 <= next_r < R) or not (0 <= next_c < C):
                continue
            if visited[next_r][next_c] or caves[next_r][next_c] == '.':
                continue

            visited[next_r][next_c] = True
            q.append((next_r, next_c))
            result.append((next_r,next_c))

    return result
            

        
def print_caves():
    for row in reversed(caves):
        for val in row:
            print(val, end="")
        print('')



for i in range(len(heights)):
    direction = 1 if i % 2 == 0 else -1
    height = heights[i]
    
    result = destroy_mineral(direction, height -1)
    if result == (-1,-1):
        continue
    else:
        for dr, dc in moves:
            next_r, next_c = result[0] + dr, result[1] + dc
            if not (0 <= next_r < R) or not (0 <= next_c < C) or caves[next_r][next_c] == ".":
                continue
            fall_mineral((next_r,next_c))


print_caves()