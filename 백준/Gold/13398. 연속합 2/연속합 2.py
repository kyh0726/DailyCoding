import sys


N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [[0,0] for _ in range(N)]
result = -1e9
# 0는 우측 기준 <- 이렇게 챙길 수 있는 최댓값
# 1은 좌측 기준 -> 이렇게 챙길 수 있는 최댓값
dp[0][0] = nums[0]
dp[N-1][1] = nums[N-1]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
    dp[N-1-i][1] = max(dp[N-i][1] + nums[N-1-i], nums[N-1-i])

for i in range(1, N-1):
    result = max(result, dp[i+1][1] + dp[i-1][0])

for i in range(N):
    result = max(result, dp[i][0])

print(result)