import sys
from collections import defaultdict

M, N = map(int, sys.stdin.readline().strip().split())

universe = defaultdict(int)

for i in range(M):
    planets = list(map(int, sys.stdin.readline().strip().split()))

    sorted_planets = sorted(planets)

    rank = {sorted_planets[i]:i for i in range(len(sorted_planets))}

    vector = tuple([rank[i] for i in planets])

    universe[vector] += 1

sum = 0


for i in universe.values():
    sum += (i * (i-1)) // 2


print(sum)