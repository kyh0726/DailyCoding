import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())


board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[[False] * 11 for _ in range(M)] for _ in range(N)]
moves = [(0,1), (0,-1), (1,0), (-1,0)]
# 해당 경로보다 
q = deque()

q.append((0,0,1,0))


min_route = 1e9
while q:
    r, c, count, crash_num = q.popleft()

    if r == N-1 and c == M-1:
        min_route = min(min_route, count)
        continue

    for dr, dc in moves:
        next_r, next_c = r + dr, c + dc

        if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
            continue

        is_crash = board[next_r][next_c]

        # 충돌 제한 넘은 경우
        if is_crash + crash_num > K:
            continue 
        if visited[next_r][next_c][is_crash + crash_num]:
            continue
        
        visited[next_r][next_c][is_crash + crash_num] = True
        q.append((next_r, next_c, count + 1, crash_num + is_crash))





        

        
        
if min_route == 1e9:
    print(-1)
else:
    print(min_route)