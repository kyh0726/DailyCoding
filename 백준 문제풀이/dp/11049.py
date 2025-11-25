import sys
#qㅂㅈㄷㄹ
N = int(sys.stdin.readline().strip())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr.append((a,b))

dp = [[0] * N for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        if start + term == N:
            break
        dp[start][start+term] = int(1e9)

        # t는 start와 start + term의 사이
        for t in range(start, start + term):
            # 이게 뭔 소리지
            # start부터 start + term 지점의 값을 기존 값과 
            # arr[start][0] * arr[t][1] * arr[start+term][1]은 t 지점에서 나눈 행렬을 다시 곱하는데 드는 비용이다.
            dp[start][start+term] = min(dp[start][start+term],
                                         dp[start][t] + dp[t+1][start+term] + arr[start][0] * arr[t][1] * arr[start+term][1])

print(dp[0][N-1])
