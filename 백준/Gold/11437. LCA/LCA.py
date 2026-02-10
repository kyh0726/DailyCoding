import sys

from collections import defaultdict

N = int(sys.stdin.readline().strip())

graph = defaultdict(list)
visited = [False] * (N+1)
visited[1] = True
parents = [i for i in range(N+1)]
level = [0] * (N+1)
stack = [1]

for i in range(N-1):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

M = int(sys.stdin.readline().strip())

# dfs 방식의 순회하여 level과 parents 넣기
while stack:
    now = stack.pop()
    for i in graph[now]:
        
        if not visited[i]:
            visited[i] = True
            parents[i] = now
            level[i] = level[now] + 1
            stack.append(i)



for i in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())

    if level[a] > level[b]:
        diff = level[a] - level[b]
        
        for i in range(diff):
            a = parents[a]
        
        for i in range(level[b]+1):
            if a == b:
                print(a)
                break
            a, b = parents[a], parents[b]

    elif level[a] < level[b]:
        diff = level[b] - level[a]
        
        for i in range(diff):
            b = parents[b]
        
        for i in range(level[a]+1):
            if a == b:
                print(a)
                break
            a, b = parents[a], parents[b]


    else:
        for i in range(level[a]+1):
            if a == b:
                print(a)
                break
            a, b = parents[a], parents[b]
