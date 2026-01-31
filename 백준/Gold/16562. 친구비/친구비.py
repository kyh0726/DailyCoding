import sys
N, M, K = map(int, sys.stdin.readline().strip().split())
uf = [i for i in range(N+1)]

answer = 0 

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        uf[x] = y
    else:
        uf[y] = x


costs = [0] + list(map(int, sys.stdin.readline().strip().split()))


for i in range(M):
    v, w = map(int, sys.stdin.readline().strip().split())
    union(v,w)


for i in range(len(costs)):
    costs[i] = [costs[i], i]


costs.sort(key=lambda x: x[0])

for cost, idx in costs:
    x = find(0)
    y = find(idx)
    if x == y:
        continue
    else:
        union(x,y)
        answer += cost


if answer <= K:
    print(answer)
else:
    print("Oh no")