import sys
from collections import defaultdict, deque


T = int(sys.stdin.readline().strip())




for i in range(T):
    N = int(sys.stdin.readline().strip())

    nodes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N-1)]
    graph = defaultdict(list)
    parents = [0] * (N+1)
    levels = [0] * (N+1)


    def bfs(start):
        visited = [False] * (N+1)
        visited[start] = True

        q = deque()
        q.append(start)

        while q:
            cur_node = q.popleft()

            for next_node in graph[cur_node]:
                if visited[next_node]:
                    continue
                
                visited[next_node] = True
                levels[next_node] = levels[cur_node] + 1
                q.append(next_node)
    
    def find_common_parents(a, b):
        a_level = levels[a]
        b_level = levels[b]
        if a_level > b_level:
            for i in range(a_level - b_level):
                a = parents[a]
        
        if a_level < b_level:
            for i in range(b_level - a_level):
                b = parents[b]
        


        for i in range(min(a_level, b_level)):
            if a == b:
                return a
            a = parents[a]
            b = parents[b]
        return a

        



    for a, b in nodes:
        graph[a].append(b)
        parents[b] = a
        levels[b] += 1
    
    for i in range(1, N+1):
        if levels[i] == 0:
            bfs(i)

    
    a, b = map(int, sys.stdin.readline().strip().split())


    result = find_common_parents(a,b)
    print(result)

    