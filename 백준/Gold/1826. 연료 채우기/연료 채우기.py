import sys
import heapq

N = int(sys.stdin.readline().strip())

fuels = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

L, P = map(int, sys.stdin.readline().strip().split())


fuels.sort(key=lambda x:x[0], reverse=True)

priority_queue = []

cur_fuel = P
counter = 0


while fuels:
    if cur_fuel >= L:
        print(counter)
        exit(0)

    if fuels[-1][0] <= cur_fuel:
        pop_fuel = fuels.pop()[1]
        heapq.heappush(priority_queue, -pop_fuel)
        continue
    
    
    if not priority_queue:
        print(-1)
        exit(0)
    else:
        pop_fuel = -heapq.heappop(priority_queue)
        cur_fuel += pop_fuel
        counter += 1




while cur_fuel < L and priority_queue:
    cur_fuel += -heapq.heappop(priority_queue)
    counter += 1



if cur_fuel >= L:
    print(counter)
else:
    print(-1)




    

