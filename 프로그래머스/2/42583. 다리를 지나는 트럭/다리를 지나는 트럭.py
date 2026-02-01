from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    cur_bridge = deque([0] * bridge_length)
    truck_weights.reverse()
    t = 0
    total = 0
    while truck_weights:
        total -= cur_bridge.popleft()
        if total + truck_weights[-1] <= weight:
            pop_weight = truck_weights.pop()
            cur_bridge.append(pop_weight)
            total += pop_weight
        else:
            cur_bridge.append(0)
            
    
        t += 1
    
    t += len(cur_bridge)
    
    return t