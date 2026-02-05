import sys
import heapq
N = int(sys.stdin.readline().strip())

tasks = []
stack = []

for i in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())

    heapq.heappush(tasks, (d, w))



while tasks:
    due_date, score = heapq.heappop(tasks)
    while stack and len(stack) >= due_date and stack[0] < score:
        heapq.heappop(stack)
    
    if len(stack) < due_date:
        heapq.heappush(stack, score)



print(sum(stack))
