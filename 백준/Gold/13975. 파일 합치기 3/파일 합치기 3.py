import sys
import heapq


T = int(sys.stdin.readline().strip())

for i in range(T):
    N = int(sys.stdin.readline().strip())
    nums = (list(map(int, sys.stdin.readline().strip().split())))
    heapq.heapify(nums)
    sum = 0
    while nums and len(nums) >= 2:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        sum += (a + b)
        heapq.heappush(nums, a + b)

    print(sum)

        