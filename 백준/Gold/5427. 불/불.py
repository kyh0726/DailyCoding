import sys
from collections import deque, defaultdict
T = int(sys.stdin.readline().strip())
moves = [(1, 0), (-1,0), (0,1), (0,-1)]
for i in range(T):
    C, R = map(int, sys.stdin.readline().strip().split())

    arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
    q = deque()
    fire_q = deque()
    fire_visited = [[False] * C for _ in range(R)]
    fires = [[1e9] * C for _ in range(R)]

    visited = [[False] * C for _ in range(R)]
    start = (0,0)

    for i in range(R):
        for j in range(C):
            if arr[i][j] == "@":
                start = (i,j)
            if arr[i][j] == "*":
                fire_q.append((i,j,0))
    def fire_bfs():
        while fire_q:
            pop_row, pop_col, time = fire_q.popleft()
            # 해당 pop_row, pop_col 좌표에 시간 값 등록
            fires[pop_row][pop_col] = min(fires[pop_row][pop_col], time)
            fire_visited[pop_row][pop_col] = True
            for dr, dc in moves:
                next_r, next_c = pop_row + dr, pop_col + dc
                
                if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
                    continue
                if arr[next_r][next_c] == "#":
                    continue
                if fire_visited[next_r][next_c]:
                    continue
                fire_visited[next_r][next_c] = True
                fire_q.append((next_r,next_c, time + 1))
    def bfs():
        start_r, start_c = start
        q.append((start_r, start_c, 0))            

        while q:
            r, c, cur_time = q.popleft()
            visited[r][c] = True
            # 그 다음에야 상근이가 움직임
            for dr, dc in moves:
                next_r, next_c = r + dr, c + dc
                if next_r == -1 or next_c == -1 or next_r == R or next_c == C:
                    return cur_time + 1
                if arr[next_r][next_c] == '#' or fires[next_r][next_c] <= cur_time + 1:
                    continue
                if visited[next_r][next_c]:
                    continue
                visited[next_r][next_c] = True
                q.append((next_r, next_c, cur_time + 1 ))
        return "IMPOSSIBLE"
    fire_bfs()
    print(bfs())

        
        
