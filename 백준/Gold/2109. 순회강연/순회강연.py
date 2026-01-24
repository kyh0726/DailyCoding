import sys
import heapq

N = int(sys.stdin.readline().strip())

target_list = []
current_date = 1
result_list = []
for i in range(N):
    p, d = map(int, sys.stdin.readline().strip().split())

    heapq.heappush(target_list, (d, -p))



while target_list:
    d, p = heapq.heappop(target_list)
    heapq.heappush(result_list, -p)

    if d < len(result_list):
        heapq.heappop(result_list)



print(sum(result_list))