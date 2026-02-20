import sys


N, M, L, K = map(int, sys.stdin.readline().strip().split())

stars = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
max_count = 0
for i in range(K):
    for j in range(K):
        count = 0

        sx, sy = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

        for l in range(K):
            target_x, target_y = stars[l]

            if sx <= target_x <= sx + L and sy <= target_y <= sy + L:
                count += 1


        max_count = max(count, max_count)


print(K - max_count)