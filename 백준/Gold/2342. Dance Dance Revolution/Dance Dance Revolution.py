import sys

arr = list(map(int, sys.stdin.readline().strip().split()))
foot = [0,0]
weights = []

MAX_NUM = 1e10

dp = [[[MAX_NUM for _ in range(5)] for _ in range(5)] for _ in range(len(arr) + 1)]

def find_dist(start, target):
    if start == target:
        return 1
    if start == 0:
        return 2
    if abs(start - target) == 2:
        return 4
    return 3

dp[0][0][0] = 0

for i in range(len(arr) - 1):
    for left in range(5):
        for right in range(5):
            
            next_target = arr[i]

            left_dist = find_dist(left, next_target)
            right_dist = find_dist(right, next_target)

            dp[i+1][next_target][right] = min(dp[i][left][right] + left_dist, dp[i+1][next_target][right])
            dp[i+1][left][next_target] = min(dp[i][left][right] + right_dist, dp[i+1][left][next_target])


print(min(min(row) for row in dp[len(arr)-1]))






