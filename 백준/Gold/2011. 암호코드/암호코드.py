import sys
sys.setrecursionlimit(10**6)

string = sys.stdin.readline().strip()

l = len(string)
dp = [0] * (l+2)
dp[0] = 1
dp[1] = 1


for k in range(1, l):
    i = k + 1
    if int(string[k]) > 0:
        dp[i] += dp[i-1]
    if  10 <= int(string[k-1]) * 10 + int(string[k]) <= 26:
        dp[i] += dp[i-2]

if string[0] == '0':
    print(0)
    exit(0)

print(dp[l] % 1000000)