import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
weights = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    weights[a][b] = 1
    weights[b][a] = -1


for j in range(1, N+1):
    for i in range(1, N+1):
        for k in range(1, N+1):
            if weights[i][j] == 1 and weights[j][k] == 1:
                weights[i][k] = 1
                weights[k][i] = -1
            if weights[i][j] == -1 and weights[j][k] == -1:
                weights[i][k] = -1
                weights[k][i] = 1

for i in range(1, N+1):
    temp = 0
    for j in range(1,N+1):
        if weights[i][j] == 0:
            temp +=1

    print(temp - 1)