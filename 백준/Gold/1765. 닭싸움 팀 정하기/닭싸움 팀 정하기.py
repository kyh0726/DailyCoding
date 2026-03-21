import sys
from collections import defaultdict
N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())

enemies = defaultdict(list)
uf = [i for i in range(N+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        uf[x] = y
    else:
        uf[y] = x



for _ in range(M):
    relation, x, y = sys.stdin.readline().strip().split()
    x, y = int(x), int(y)
    if relation == "E":
        for enemy in enemies[x]:
            union(enemy, y)
        for enemy in enemies[y]:
            union(enemy, x)
        
        enemies[x].append(y)
        enemies[y].append(x)
    
    else:
        union(x,y)

result = set()

for i in range(1, N+1):
    result.add(find(i))


print(len(result))