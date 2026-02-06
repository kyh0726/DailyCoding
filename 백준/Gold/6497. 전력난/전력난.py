import sys
import heapq

while True:
    m, n = map(int, sys.stdin.readline().strip().split())

    if m == 0 and n == 0:
        break

    uf = [i for i in range(m)]
    max_cost = 0
    save_cost = 0

    def find(x):
        if uf[x] == x:
            return x
        uf[x] = find(uf[x])
        return uf[x]


    def union(a, b):
        a = find(a)
        b = find(b)
        minP, maxP = min(a, b), max(a, b)
        uf[maxP] = minP



    distances = []

    for i in range(n):
        x,y,z = map(int, sys.stdin.readline().strip().split())
        max_cost += z
        heapq.heappush(distances, (z,x,y))


    while distances:
        
        z, x, y = heapq.heappop(distances)


        if find(x) == find(y):
            continue
        
        union(x,y)
        save_cost += z



    print(max_cost - save_cost)

