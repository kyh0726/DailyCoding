import sys
from collections import deque, defaultdict
import heapq
N, M = map(int, sys.stdin.readline().strip().split())

road_info = defaultdict(list)

roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]



for idx, (a, b) in enumerate(roads):
    road_info[a].append((b, idx))
    road_info[b].append((a, idx))

visited = [False] * (N+1)

INF = 10**15

def dijkstra():
    distances = [INF] * (N+1)
    distances[1] = M - 1

    cur_road_num = 1
    cur_dist = M -1 

    q = []
    heapq.heappush(q, (cur_dist, cur_road_num))

    while q:
        pop_dist, pop_road_num = heapq.heappop(q)

        if distances[pop_road_num] < pop_dist:
            continue
        
        if pop_road_num == N:
            return pop_dist

        distances[pop_road_num] = pop_dist

        road_idx = pop_dist % M

        for next_road_num, next_road_idx in road_info[pop_road_num]:
            add_dist = next_road_idx - road_idx if next_road_idx > road_idx else M - (road_idx - next_road_idx)
            next_dist = pop_dist + add_dist

            if next_dist < distances[next_road_num]:
                heapq.heappush(q, (next_dist, next_road_num))


print(dijkstra() - M + 1)






    

    
    
    
