import sys

N, H = map(int, sys.stdin.readline().strip().split())
acc_sum = [0] * (H+1)
for i in range(N):
    target = int(sys.stdin.readline().strip())
    if i % 2 == 0:
        acc_sum[0] += 1
        acc_sum[target] -= 1
    else:
        acc_sum[H-target] += 1
min_val = 50000000
min_num = 0

cur_sum = 0
for i in range(H):
    cur_sum += acc_sum[i]
    if cur_sum < min_val:
        min_val = cur_sum
        min_num = 1
    elif cur_sum == min_val:
        min_num += 1


print(min_val, min_num)