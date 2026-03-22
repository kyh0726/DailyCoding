import sys

input = sys.stdin.readline

M, N = map(int, input().split())

size = 2 * M - 1
diff = [0] * (size + 1)

for _ in range(N):
    zero, one, two = map(int, input().split())

    diff[zero] += 1
    diff[zero + one] += 1

# 누적합으로 실제 성장량 복원
line = [0] * size
cur = 0
for i in range(size):
    cur += diff[i]
    line[i] = cur

top_row = [line[i] + 1 for i in range(M - 1, size)]

output = []
output.append(" ".join(map(str, top_row)))

right_part = list(map(str, top_row[1:]))
for i in range(1, M):
    row = [str(line[M - 1 - i] + 1)] + right_part
    output.append(" ".join(row))

print("\n".join(output))