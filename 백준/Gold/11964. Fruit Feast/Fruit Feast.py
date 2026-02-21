import sys
from collections import deque

T, A, B = map(int, sys.stdin.readline().strip().split())

fruits = [A,B]

visited = [[0] * (2) for _ in range(T+1)]

start = 0
q = deque()
q.append((start, 0))
max_node = 0

while q:
    pop_node, drink_water = q.popleft()
    max_node = max(max_node, pop_node)


    if visited[pop_node][0] or visited[pop_node][1] and (drink_water == 1):
        continue
    
    if visited[pop_node][0] and drink_water == 0:
        continue
    
    visited[pop_node][drink_water] = 1

    if not drink_water:
        q.append((pop_node // 2, drink_water + 1))

    for fruit in fruits:
        next_node = pop_node + fruit
        if next_node > T:
            continue
        q.append((next_node, drink_water))
    


print(max_node)