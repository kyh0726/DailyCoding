import sys
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))


if K >= N:
  print(0)
  exit(0)
arr.sort()
dist = []
for i in range(1, N):
  dist.append(arr[i] - arr[i-1])


dist.sort(reverse=True)
for _ in range(K-1):
  dist.pop(0)

print(sum(dist))

