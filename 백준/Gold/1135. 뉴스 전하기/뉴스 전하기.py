import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

people = list(map(int, sys.stdin.readline().strip().split()))

costs = [0 for _ in range(N)]

graph = defaultdict(list)


for idx,val in enumerate(people):
    if val == -1:
        continue
    graph[val].append(idx)




def dfs(cur_node):

    for next_node in graph[cur_node]:
        dfs(next_node)

    if len(graph[cur_node]) == 0:
        costs[cur_node] = 1
    else:
        temp = []
        for next_node in graph[cur_node]:
            temp.append(costs[next_node])
        
        temp.sort(reverse=True)

        max_num = 0
        for i in range(len(temp)):
            max_num = max(max_num, i + temp[i] + 1)

        costs[cur_node] = max_num

    

    

dfs(0)
print(costs[0] -1)