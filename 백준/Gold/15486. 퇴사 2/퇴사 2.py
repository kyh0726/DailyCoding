import sys

N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]   
dp = [0] * (N+1)

profit = 0

for i in range(N):
    # profit = 오늘까지 벌 수 있는 돈
    profit = max(profit, dp[i])

    # 퇴사일 넘김
    if i + arr[i][0] > N:
        continue

    # i = 현재 날짜
    # arr[i][0] = 소요되는 날짜
    # i + arr[i][0] 현재 날짜에서 일 해서 예상 데드라인
    # profit은 
    dp[i + arr[i][0]] = max(profit + arr[i][1], dp[i + arr[i][0]])
print(max(dp))