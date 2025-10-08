import sys
import heapq
input = sys.stdin.readline

N = int(sys.stdin.readline().strip())
q = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(q, (x,y))

sum = 0
start = -1e10
end = -1e10
while q:
    next_start, next_end = heapq.heappop(q)
    if next_start > end:
        sum += end - start
        start = next_start
        end = next_end
    else:
        if end < next_end:
            end = next_end


sum += end - start

print(int(sum))