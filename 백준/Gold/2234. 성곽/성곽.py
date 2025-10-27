import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
moves = [(0,-1), (-1,0), (0,1), (1,0)]
visited = [[0] * N for _ in range(M)]
visit_count = 0
max_count = 0
max_sum = 0
sums = [0] * (N * M + 1)
def find_near_wall(val):
    temp = val
    arr = []
    for i in range(4):
        remain_num = temp % 2
        temp = temp // 2
        arr.append(remain_num) 

    return arr


def find_room_size(row, col):
    global visit_count
    global max_count
    visit_count += 1
    q = deque()
    q.append((row, col))
    visited[row][col] = visit_count
    count = 1

    while q:
        r, c = q.popleft()
        avail_arr = find_near_wall(board[r][c])

        for i in range(4):
            dr, dc = moves[i]
            next_r, next_c = r + dr, c + dc
            if next_r < 0 or next_c < 0 or next_r >= M or next_c >= N:
                continue
            if avail_arr[i]:
                continue

            if visited[next_r][next_c]:
                continue
            visited[next_r][next_c] = visit_count
            count += 1
            q.append((next_r,next_c))

    max_count = max(max_count, count)
    sums[visit_count] = count



for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        find_room_size(i,j)


for i in range(M):
    for j in range(N):
        r,c = i,j

        for dr, dc in moves:
            next_r, next_c = r + dr, c + dc

            if next_r < 0 or next_c < 0 or next_r >= M or next_c >= N:
                continue
            if visited[next_r][next_c] != visited[r][c]:
                max_sum = max(sums[visited[next_r][next_c]] + sums[visited[r][c]], max_sum)

print(visit_count)
print(max_count)
print(max_sum)

