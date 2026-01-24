import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline().strip())
nodes = defaultdict(list)
visited = [False] * (N+1)
dp = [[0,0] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)


def dfs(start):
    global nodes
    global visited    
    visited[start] = True

    if len(nodes[start]) == 0:
        dp[start][0] = 0
        dp[start][1] = 1
    else:
        for next_node in nodes[start]:
            if visited[next_node] == 0:
                dfs(next_node)
                dp[start][1] += min(dp[next_node][0], dp[next_node][1])
                dp[start][0] += dp[next_node][1]
        dp[start][1] += 1


dfs(1)
print(min(dp[1][0], dp[1][1]))
