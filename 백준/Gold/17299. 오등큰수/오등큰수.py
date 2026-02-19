import sys
from collections import defaultdict
N = int(sys.stdin.readline().strip())
counts = defaultdict(int)
nums = list(map(int, sys.stdin.readline().strip().split()))

for val in nums:
    counts[val] += 1


stack = []
result = [-1] * (N)


for idx, num in enumerate(nums):
    cur_count = counts[num]

    while stack and counts[nums[stack[-1]]] < cur_count:
        pop_idx = stack.pop()
        result[pop_idx] = num
    
    stack.append(idx)
        

for val in result:
    print(val, end=" ")