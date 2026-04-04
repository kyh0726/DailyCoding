import sys
from collections import deque
n,w,l = list(map(int, sys.stdin.readline().strip().split()))

trucks = list(map(int, sys.stdin.readline().strip().split()))
trucks.reverse()
bridge = deque()
total_weight = 0

for i in range(w):
    bridge.append(0)


counter = 0
while trucks:
    cur_truck = trucks.pop()
    total_weight -= bridge.popleft()

    while total_weight + cur_truck > l:
        total_weight -= bridge.popleft()
    

    while len(bridge) < w - 1:
        bridge.append(0)
        counter += 1
    
    bridge.append(cur_truck)
    total_weight += cur_truck
    counter += 1

while total_weight > 0:
    counter += 1
    total_weight -= bridge.popleft()

print(counter)

    
