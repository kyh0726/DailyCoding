import sys
import heapq
from collections import defaultdict

T = int(sys.stdin.readline().strip())


for _ in range(T):
    k = int(sys.stdin.readline().strip())
    
    min_heap = []
    max_heap = []
    visited = defaultdict(int)

    for __ in range(k):
        cmd, target = sys.stdin.readline().strip().split()
        target = int(target)
        if cmd == "I":
            heapq.heappush(min_heap, target)
            heapq.heappush(max_heap, -target)
            visited[target] += 1
        else:
            if target == 1:
                while max_heap and visited[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    pop_node = -heapq.heappop(max_heap)
                    visited[pop_node] -= 1
            else:
                while min_heap and visited[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    pop_node = heapq.heappop(min_heap)
                    visited[pop_node] -= 1
    

    while min_heap and visited[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and visited[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

        
    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))

