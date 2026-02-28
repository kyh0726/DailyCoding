# 11:28

import sys
import heapq
N, C = map(int, sys.stdin.readline().strip().split())

pipes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
def find_dist(pos1,pos2):
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

visited = [False] * (N)
min_dist = [float('inf')] * N
min_dist[0] = 0

result = 0
count = 0

for _ in range(N):
    new_idx = -1
    cur_dist = 1e10

    for i in range(N):
        if not visited[i] and min_dist[i] < cur_dist:
            cur_dist = min_dist[i]
            new_idx = i

    
    if new_idx == -1:
        break

    visited[new_idx] = True
    result += cur_dist
    count += 1


    for i in range(N):
        if visited[i]:
            continue
        dist = find_dist(pipes[i], pipes[new_idx])
        
        if dist >= C and dist < min_dist[i]:
            min_dist[i] = dist

if count == N:
    print(result)   
else:
    print(-1)
