import sys


N, M = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split()))
sum = [0] * (N)
sum[0] = arr[0] % M
for i in range(1,N):
    sum[i] = (sum[i-1] + arr[i]) % M
answer = 0

for i in range(M):
    cnt = 0
    for j in range(N):
        if sum[j] == i:
            cnt += 1
    
    if i == 0:
        answer += cnt
    if cnt > 1:
        answer += (cnt * (cnt - 1)) // 2


print(answer)
