import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline().strip())

vil_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
visited = [False] * (N+1)
nodes = defaultdict(list)
dp = [[0,0] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)



def dfs(start):
    
    visited[start] = True

    if len(nodes[start]) == 0:
        dp[start][0] = 0
        dp[start][1] = vil_list[start]

    for next_node in nodes[start]:
        if not visited[next_node]:
            dfs(next_node)
            dp[start][0] += max(dp[next_node][0], dp[next_node][1])
            dp[start][1] += dp[next_node][0]
    
    dp[start][1] += vil_list[start]


dfs(1)
print(max(dp[1][0], dp[1][1]))



