import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
visited = [False] * (n+1)
levels = [0] * (n+1)
total = 0


m = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)



def dfs():
    global total
    stack = []
    stack.append(1)
    visited[1] = True

    while stack:
        cur_node = stack.pop()
        total += 1


        if levels[cur_node] == 2:
            continue

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True
                levels[next_node] = levels[cur_node] + 1


dfs()

print(total-1)