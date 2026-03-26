import sys
from collections import defaultdict,deque

N, M = map(int, sys.stdin.readline().strip().split())

relations = defaultdict(list)
priorities = defaultdict(int)
prerequisites = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
results = [0] * (N+1)


for prerequisite in prerequisites:
    pre, post = prerequisite
    priorities[post] += 1
    relations[pre].append(post)

q = deque()

for i in range(1, N+1):
    if priorities[i] == 0:
        q.append((i, 0))
    


while q:
    pop_node, count = q.popleft()
    results[pop_node] = count + 1


    for next_node in relations[pop_node]:
        priorities[next_node] -= 1
        if priorities[next_node] == 0:
            q.append((next_node, count + 1))


print(*results[1:])