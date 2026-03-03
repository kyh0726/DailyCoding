import sys
from collections import deque, defaultdict

# 방문했을 때 locked인 곳은 check해두고, .

N, M = map(int, sys.stdin.readline().strip().split())
moves = [(0,1), (0,-1), (1,0),(-1,0)]
rooms = [[0] * (N+1) for _ in range(N+1)]

will_visit = [[False]*(N+1) for _ in range(N+1)]
visited = [[False]*(N+1) for _ in range(N+1)]
locked = [[True]*(N+1) for _ in range(N+1)]

input_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
switches = defaultdict(list)
for x,y,a,b in input_list:
    switches[(x,y)].append((a,b))


q = deque()
q.append((1,1))

bright_areas = set()

count = 0
bright_areas.add((1,1))
while q:
    row, col = q.popleft()
    if visited[row][col]:
        continue
    visited[row][col] = True

    # 갈 수 있는 곳 활성화
    for r, c in switches[(row,col)]:
        if locked[r][c]:
            locked[r][c] = False
            bright_areas.add((r,c))
        if will_visit[r][c] and not visited[r][c]:
            q.append((r,c))


    for dr, dc in moves:
        next_r, next_c = row + dr, col + dc
        if next_r <= 0 or next_c <= 0 or next_r > N or next_c > N or visited[next_r][next_c]:
            continue

        # 잠겨있으면 추가만 해두기
        if not locked[next_r][next_c]:
            q.append((next_r,next_c))
            continue
        # 안잠겨있으면 방문 예정 표시
        else:
            will_visit[next_r][next_c] = True
        


print(len(bright_areas))

