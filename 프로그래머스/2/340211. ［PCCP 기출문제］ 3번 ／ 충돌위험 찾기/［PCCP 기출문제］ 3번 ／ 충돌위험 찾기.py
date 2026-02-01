from collections import deque

def solution(points, routes):
    answer = 0
    q = deque()
    
    
    def find_next_pos(cur_pos, end_pos):
        if cur_pos[0] != end_pos[0]:
            if cur_pos[0] < end_pos[0]:
                return (cur_pos[0] + 1, cur_pos[1])
            else:
                return (cur_pos[0] - 1, cur_pos[1])
        
        if cur_pos[1] != end_pos[1]:
            if cur_pos[1] < end_pos[1]:
                return (cur_pos[0], cur_pos[1] + 1)
            else:
                return (cur_pos[0], cur_pos[1] - 1)
        
        return (cur_pos[0], cur_pos[1])

    t = [False] * 1000
    start_col = set()
    for route in routes:
        if not t[route[0]]:
            t[route[0]] = True
        else:
            start_col.add(route[0])
        
        
        temp = deque()
        for i in route:
            temp.append((points[i-1]))
        q.append(temp)
        
    answer += len(start_col)
    while q:
        
        q_len = len(q)
        
        visited = [[False] * 101 for _ in range(101)]
        col_set = set()
        for i in range(q_len):    
            pop_route = q.popleft()
            cur_pos, end_pos = pop_route[0], pop_route[1]
            
            next_r, next_c = find_next_pos(cur_pos, end_pos)
            next_pos = [next_r, next_c]
            
            
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
            else:
                col_set.add((next_r,next_c))


            
            if (next_r, next_c) == (end_pos[0], end_pos[1]):
                if len(pop_route) >= 3:
                    pop_route.popleft()
                    q.append(pop_route)
                    continue
                else:
                    continue
            
                
            
            pop_route[0] = next_pos
            q.append(pop_route)
        
        answer += len(col_set)
                
            
            
            
    
    
    
    return answer