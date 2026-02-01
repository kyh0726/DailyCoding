from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리 상태를 관리하는 큐 (0은 빈 공간을 의미)
    bridge = deque([0] * bridge_length)
    # 대기 트럭 큐
    trucks = deque(truck_weights)
    
    current_weight = 0 # 현재 다리 위 트럭들의 무게 합 (핵심 최적화 포인트)
    
    while bridge:
        time += 1
        # 1. 다리 끝에서 트럭이 나감
        exiting_truck = bridge.popleft()
        current_weight -= exiting_truck
        
        # 2. 새로운 트럭이 들어올 수 있는지 확인
        if trucks:
            if current_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                # 무게 때문에 못 들어오면 빈 공간(0)을 채움
                bridge.append(0)
                
    return time