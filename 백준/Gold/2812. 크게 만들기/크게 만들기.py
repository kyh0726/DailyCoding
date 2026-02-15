import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

nums = deque(list(sys.stdin.readline().strip()))

last_idx = 0

stack = []
count = 0
while nums:
    pop_num = nums.popleft()
    while stack and stack[-1] < pop_num:
        if count == K:
            break
        stack.pop()
        count += 1
    
    stack.append(pop_num)

for i in range(K - count):
    stack.pop()


for val in stack:
    print(val,end="")    


