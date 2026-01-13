import sys


N = int(sys.stdin.readline().strip())


# 맨 위 모서리 : 3개의 면
# 그 외의 기둥 모서리 : 2개의 면
# 다른 면들 : 1개의 면

dices = list(map(int, sys.stdin.readline().strip().split()))
adjs_3 = [[0,1,2], [0,2,4], [0,3,4], [0,1,3], [5,1,2], [5,2,4], [5,3,4], [5,1,3]]
adjs_2 = [[0,1], [0,2], [0,3], [0,4], [1,2], [2,4], [3,4], [1,3], [5,1], [5,2], [5,3], [5,4]]


min_adjs_3 = 1e10
min_adjs_2 = 1e10
min_adjs_1 = min(dices)

for row in adjs_3:
    temp = 0
    for idx in row:
        temp += dices[idx]

    min_adjs_3 = min(min_adjs_3, temp)

for row in adjs_2:
    temp = 0
    for idx in row:
        temp += dices[idx]

    min_adjs_2 = min(min_adjs_2, temp)

total_num = N * N * 5 - (N*8 - 4)




if N == 1:
    print(sum(dices) - max(dices))
    exit(0)

if N == 2:
    print(min_adjs_3 * 4 + min_adjs_2 * 4)
    exit(0)


min_adjs_3_num = 4
min_adjs_2_num = N * 8 - 8 - 4
min_adjs_1_num = total_num - min_adjs_2_num - min_adjs_3_num


print(min_adjs_3_num * min_adjs_3 + min_adjs_2_num * min_adjs_2 + min_adjs_1_num * min_adjs_1)

