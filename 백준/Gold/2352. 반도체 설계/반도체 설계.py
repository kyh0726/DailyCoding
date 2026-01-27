import sys


N = int(sys.stdin.readline().strip())
ports = list(map(int, sys.stdin.readline().strip().split()))

dp = [ports[0]]

def binary_search(arr, target_val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        
        if target_val > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return start

for i in range(N):
    if dp[-1] < ports[i]:
        dp.append(ports[i])
    else:
        idx = binary_search(dp, ports[i])
        dp[idx] = ports[i]


print(len(dp))