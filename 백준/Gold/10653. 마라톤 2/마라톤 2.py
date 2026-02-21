import sys

N, K = map(int, sys.stdin.readline().strip().split())
INF = 1e10
check_points = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
dists = [[0]*N for _ in range(N)]
dp = [[INF] * (K+1) for _ in range(N)]

def calc_distance(start, end):
    start_r, start_c = start
    end_r, end_c = end

    return abs(start_r - end_r) + abs(start_c - end_c)

for i in range(K+1):
    dp[0][i] = 0


for i in range(N):
    for j in range(i+1, N):
        dists[i][j] = calc_distance(check_points[i], check_points[j])



for cur_node in range(1, N):
    for step in range(K+1):
        if cur_node - step < 0:
            break
        
        for cur_step in range(step, K+1):
            dp[cur_node][cur_step] = min(dp[cur_node - step - 1][cur_step - step] + dists[cur_node - step - 1][cur_node], dp[cur_node][cur_step])

print(min(dp[N-1]))