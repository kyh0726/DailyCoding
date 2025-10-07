import sys
C, N = map(int, input().split())

dp = [float('inf')] * 3000
dp[0] = 0


for i in range(N):
  cost, num = map(int, sys.stdin.readline().strip().split())

  for j in range(num, 3000):
    dp[j] = min(dp[j], dp[j-num] + cost)



print(min(dp[C:]))
