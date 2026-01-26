import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
dp = [0 for i in range(N+1)]
result = 0

# gpt의 알고리즘 멘탈모델 예시

# N = 9
# VIP = [4, 7]

# 구간 분해:
# [1 2 3] (VIP) [5 6] (VIP) [8 9]


vip_seats = []

for i in range(M):
    vip_seats.append(int(sys.stdin.readline().strip()))

dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if M > 0:
    prev_idx = 0
    
    for vip_seat in vip_seats:
        answer *= dp[vip_seat - 1 - prev_idx] 
        prev_idx = vip_seat

    answer *= dp[N-prev_idx]
else:
    answer = dp[N]
print(answer)   