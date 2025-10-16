import sys
from collections import defaultdict, deque

N =  int(sys.stdin.readline().strip())
graph = defaultdict(list)
min_score = 500
min_list = []
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1:
        break

    
    graph[a].append(b)
    graph[b].append(a)

def find_score(node_num):
    visited = [False] *  (N+1)
    max_count = 0
    q = deque()
    q.append((node_num, 0))
    visited[node_num] = True

    while q:
        pop_node, count = q.popleft()
        max_count = max(max_count, count)

        for next_node in graph[pop_node]:
            if visited[next_node]:
                continue
            q.append((next_node, count + 1))
            visited[next_node] = True
    
    return max_count


for i in range(1, N+1):
    count = find_score(i)
    if count < min_score:
        min_list = [i]
        min_score = count
    elif count == min_score:
        min_list.append(i)


print(min_score, len(min_list))
print(*min_list, sep=" ")