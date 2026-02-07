import sys
import heapq

T = int(sys.stdin.readline().strip())


for i in range(T):
    M = int(sys.stdin.readline().strip())
    nums = []
    temp = []
    min_heap = []
    max_heap = []
    for i in range(M//10 + 1):
       nums.extend(list(map(int, sys.stdin.readline().strip().split()))) 
    cur_mid = 0
    for i in range(0, len(nums)):
        if i == 0:
            cur_mid = nums[i]
            temp.append(cur_mid)
            heapq.heappush(min_heap, nums[i])
            heapq.heappush(max_heap, -nums[i])
            continue
        
        # 최소 힙에는 현재 중간 값보다 더 큰 값들 저장
        if cur_mid < nums[i]:
            heapq.heappush(min_heap, nums[i])

        # 최대 힙에는 현재 중간 값보다 더 작은 값들 저장
        else:
            heapq.heappush(max_heap, -nums[i])

        
        if i % 2 == 0:
            if len(min_heap) < len(max_heap):
                pop_val = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -max_heap[0])
            if len(min_heap) > len(max_heap):
                pop_val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_heap[0])
            
            cur_mid = min_heap[0]
            temp.append(cur_mid)
    
    print(len(temp))
    for i in range(len(temp)):
        if (i+1)%10 == 0 or i == len(temp) - 1:
            print(temp[i])
            continue
        print(temp[i], end=" ")





