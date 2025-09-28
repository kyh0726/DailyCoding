import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])

for i in range(N):
    M = int(sys.stdin.readline().strip())
    parent = defaultdict()
    number = defaultdict()


    for i in range(M):
        a, b = sys.stdin.readline().strip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
