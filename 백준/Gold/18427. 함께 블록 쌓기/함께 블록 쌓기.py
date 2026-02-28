import sys

N, M, H = map(int, sys.stdin.readline().strip().split())

blocks = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N)]




for i in range(N):
    for block in blocks[i]:
        if i == 0:
            if block > H:
                continue
            dp[i][block] = 1
            dp[i][0] = 1
            continue
        
        # 이전에 선택한 값에 새로운 블록을 케이스
        for j in range(H+1):
            next_block = block + j

            if next_block > H :
                continue
            dp[i][next_block] += dp[i-1][j]

    # 선택 안하는 케이스
    if i == 0:
        continue
    for k in range(H+1):
        dp[i][k] += dp[i-1][k]


print(dp[N-1][H]%10007)