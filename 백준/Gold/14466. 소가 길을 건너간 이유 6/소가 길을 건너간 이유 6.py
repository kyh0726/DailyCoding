import sys
from collections import deque, defaultdict

N,K,R = map(int, sys.stdin.readline().strip().split())


board = [[-1] * N for _ in range(N)]

roads = [list(map(lambda x:int(x)-1, sys.stdin.readline().strip().split())) for _ in range(R)]

cannot_go = defaultdict(int)

for r,c,next_r,next_c in roads:
    cannot_go[(r,c,next_r,next_c)] = 1
    cannot_go[(next_r,next_c,r,c)] = 1



cows = [list(map(lambda x:int(x)-1, sys.stdin.readline().strip().split())) for _ in range(K)]
cow_set = set()
for cow in cows:
    cow_set.add(tuple(cow))
cow_number = len(cows)
result = cow_number*(cow_number-1)//2

visited = [[False] * N for _ in range(N)]

moves = [(0,1), (0,-1), (1,0),(-1,0)]
def bfs(position):
    global result
    r,c = position
    q = deque()
    q.append((r,c))
    counter = 0
    visited[r][c] = True

    while q:
        row, col = q.popleft()

        if (row,col) in cow_set:
            counter += 1
        for dr, dc in moves:
            next_r, next_c = row + dr, col + dc

            
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
                continue
            if visited[next_r][next_c]:
                continue
            if cannot_go[(row,col,next_r,next_c)]:
                continue
            
            visited[next_r][next_c] = True
            q.append((next_r,next_c))


    result -= counter * (counter - 1) // 2
for cow in cows:
    if visited[cow[0]][cow[1]]:
        continue
    bfs(cow)

print(result)
