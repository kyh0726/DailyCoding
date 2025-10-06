from collections import deque, defaultdict

def solution(n, path, order):
    """모든 동굴 방을 방문할 수 있는지 확인"""
    
    # 그래프 구성
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    # 선행 조건 매핑
    unlocks = {}      # unlocks[A] = B : A 방문 시 B 활성화
    needs = {}        # needs[B] = A : B 가려면 A 필요
    
    for required, target in order:
        unlocks[required] = target
        needs[target] = required
        
        # 시작점이 잠기면 불가능
        if target == 0:
            return False
    
    # BFS 초기화
    visited = set([0])
    waiting = {}  # 대기 중인 방
    queue = deque([0])
    
    # BFS 탐색
    while queue:
        current = queue.popleft()
        
        # 현재 방을 기다리던 방 활성화
        if current in unlocks:
            next_room = unlocks[current]
            if next_room in waiting:
                queue.append(next_room)
                del waiting[next_room]
                visited.add(next_room)
                queue.append(next_room)
        
        # 인접 방 탐색
        for next_room in graph[current]:
            if next_room in visited:
                continue
            
            # 선행 조건 확인
            if next_room in needs:
                required = needs[next_room]
                
                # 선행 조건 미충족 → 대기
                if required not in visited:
                    waiting[next_room] = required
                    continue
            
            # 방문 처리
            visited.add(next_room)
            queue.append(next_room)
    return len(visited) == n