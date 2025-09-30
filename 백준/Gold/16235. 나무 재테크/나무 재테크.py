import sys
from collections import defaultdict, deque

N, M, K = map(int, sys.stdin.readline().strip().split())
maps = [[5] * (N+1) for _ in range(N+1)]
add_maps = []
add_maps.append([0] * (N+1))
adjs = [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)]
for i in range(N):
    add_maps.append([0] + list(map(int, sys.stdin.readline().strip().split())))


places = [[[] for _ in range(N+1)] for _ in range(N+1)]


for i in range(M):
    r, c, age = map(int, sys.stdin.readline().strip().split())
    places[r][c].append(age)

for _ in range(K):
    # 양분 먹기
    dead_places = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            ages = places[i][j]
            ages.sort()
            new_ages = []

            for age in ages:
                if maps[i][j] >= age:
                    maps[i][j] -= age
                    new_ages.append(age + 1)
                else:
                    dead_places.append((i,j,age))
            places[i][j] = new_ages
    # 죽은 나무들 양분으로 변하기
    for dead_place in dead_places:        
        r,c,age = dead_place
        nutrient = age // 2
        maps[r][c] += nutrient

    # 가을에는 나무 번식
    for i in range(1,N+1):
        for j in range(1,N+1):
            ages = places[i][j]
            for age in ages:
                if age % 5 != 0:
                    continue
                for dr, dc in adjs:
                    next_r, next_c = i + dr, j + dc
                    if next_r > N or next_c > N or next_r < 1 or next_c < 1:
                        continue
                    places[i+dr][j+dc].append(1)

    # 겨울에 양분 주기
    for i in range(1, N+1):
        for j in range(1, N+1):
            maps[i][j] += add_maps[i][j]

sum = 0
for i in range(1,N+1):
    for j in range(1, N+1):
        ages = places[i][j]
        sum += len(ages)
        
print(sum)

