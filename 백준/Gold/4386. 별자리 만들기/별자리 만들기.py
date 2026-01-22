import sys
import math
import heapq

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calc_distance(a:Pos, b:Pos):
    return math.sqrt(abs(a.x - b.x) * abs(a.x - b.x) + abs(a.y - b.y) * abs(a.y - b.y))

def find(x):
    if nodes[x] == x:
        return x
    nodes[x] = find(nodes[x])
    return nodes[x]

def union(x,y):
    x = nodes[x]
    y = nodes[y]
    if x != y:
        nodes[x] = y


N = int(sys.stdin.readline().strip())
pos_list = []
dist_list = []
nodes = [i for i in range(N)]
result = 0

for i in range(N):
    pos_x, pos_y = map(float, sys.stdin.readline().strip().split())
    pos_list.append(Pos(pos_x, pos_y))    


for i in range(len(pos_list)):
    for j in range(i + 1, len(pos_list)):
        heapq.heappush(dist_list, (calc_distance(pos_list[i], pos_list[j]), i, j))


while dist_list:
    dist, x, y = heapq.heappop(dist_list)
    if find(x) != find(y):
        union(x,y)
        result += dist

print(round(result, 2))