import sys
from collections import deque, defaultdict

DIRTY = '*'
CLEAN = '.'
FURNITURE = 'x'
START = 'o'
moves = [(0,1), (0,-1), (1,0),(-1,0)]
results = []
while True:
    C, R = map(int, sys.stdin.readline().strip().split())

    if (R,C) == (0,0):
        break



    board = [list(sys.stdin.readline().strip()) for _ in range(R)]

    dirty_rooms = []
    start_pos = [0,0]



    for r in range(R):
        for c in range(C):
            if board[r][c] == DIRTY:
                dirty_rooms.append((r,c))
            if board[r][c] == START:
                start_pos = [r,c]
    
    dirty_rooms.append(start_pos)
    # 경로 미리 생성
    distances = defaultdict(int)

    for start_r, start_c in dirty_rooms:
        visited= [[False]*C for _ in range(R)]
        q = deque()
        q.append((start_r,start_c,0))
        visited[start_r][start_c] = True
        while q:
            r, c, count = q.popleft()

            for dr, dc in moves:
                next_r, next_c = r + dr, c + dc

                if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
                    continue
                if board[next_r][next_c] == FURNITURE or visited[next_r][next_c]:
                    continue

                q.append((next_r,next_c,count+1))
                visited[next_r][next_c] = True
                distances[(start_r,start_c,next_r,next_c)] = count + 1

    
    dirty_rooms.pop()
    min_cost = 1e10
    dfs_visited = [[False]*C for _ in range(R)]
    def dfs(cur_pos, cur_cost,count):
        global min_cost
        if cur_cost >= min_cost:
            return

        if count == len(dirty_rooms):
            min_cost = min(min_cost,cur_cost)
            return
        

        for next_r,next_c in dirty_rooms:
            if dfs_visited[next_r][next_c]:
                continue
            
            dfs_visited[next_r][next_c] = True

            next_pos = (next_r,next_c)

            add_cost = distances[(cur_pos[0],cur_pos[1],next_r,next_c)]
            if add_cost == 0:
                continue

            next_cost = cur_cost + add_cost
            dfs(next_pos, next_cost, count + 1)

            dfs_visited[next_r][next_c] = False

    dfs(start_pos, 0, 0)

    if min_cost == 1e10:
        min_cost = -1
    results.append(min_cost)


for result in results:
    print(result)

    

    