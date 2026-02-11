import sys
from collections import defaultdict


N, M = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)

max_num = 0
max_list = []

for i in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[b].append(a)




def dfs(start):
    global N
    stack = []
    stack.append(start)
    visited = [False] * (N+1)
    visited[start] = True
    temp = 0
    while stack:
        pop_val = stack.pop()
        temp += 1
        for next_val in graph[pop_val]:
            if not visited[next_val]:
                visited[next_val] = True
                stack.append(next_val)
    return temp


for i in range(1,N+1):
    temp = dfs(i)
    if temp > max_num:
        max_num = temp
        max_list = [i]
    elif temp == max_num:
        max_list.append(i)

        

print(*sorted(max_list))
