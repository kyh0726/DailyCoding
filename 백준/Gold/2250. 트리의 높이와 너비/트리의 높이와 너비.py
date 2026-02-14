import sys
from collections import defaultdict


graph = defaultdict(list)

N = int(sys.stdin.readline().strip())
levels = defaultdict(list)
count = 0
isRoot = [True] * (N+1)
# 너비 계산
# 열의 값들이 중위순회한 순서대로 값들이 놓인다

def in_order_traverse(root, level):
    global count
    left_node = graph[root][0]
    right_node = graph[root][1]

    if left_node != -1:
        in_order_traverse(left_node, level + 1)

    levels[level].append(count)
    count += 1
    
    if right_node != -1:
        in_order_traverse(right_node, level + 1)



for i in range(N):
    parent, left, right = map(int, sys.stdin.readline().strip().split())
    if left != -1:
        isRoot[left] = False
    if right != -1:
        isRoot[right] = False
    graph[parent] = [left, right]


for i in range(1, N+1):
    if isRoot[i]:
        in_order_traverse(i, 1)


max_gap = 1
max_level = 1
for i in range(1, N+1):
    sorted_pos = sorted(levels[i])

    if len(sorted_pos) < 2:
        continue

    if sorted_pos[-1] - sorted_pos[0] + 1 > max_gap:
        max_gap = sorted_pos[-1] - sorted_pos[0] + 1
        max_level = i

print(max_level)
print(max_gap)


