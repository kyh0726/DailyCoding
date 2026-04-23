import copy
from collections import defaultdict, deque

def solution(n, infection, edges, k):
    A = 1
    B = 2
    C = 3
    
    answer = 0
    cases = []
    def make_cases(case):
        if len(case) == k:
            cases.append(case)
            return
    
        for val in [1,2,3]:
            copy_case = copy.deepcopy(case)
            copy_case.append(val)
            make_cases(copy_case)
    graph = defaultdict(list)
    
    for x,y,t in edges:
        graph[x].append((y,t))
        graph[y].append((x,t))
        
    
    
    make_cases([])
    
    for cur_case in cases:
        cur_infection = set([infection])
        
        for cur_pipe in cur_case:
            
            q = deque()
            visited = [False] * (n+1)
            for infected_node in cur_infection:
                q.append(infected_node)
                visited[infected_node] = True
            
            while q:
                pop_node = q.popleft()
                
                for next_node, next_pipe_type in graph[pop_node]:
                    if next_pipe_type != cur_pipe:
                        continue
                    if visited[next_node]:
                        continue
                    if next_node not in cur_infection:
                        cur_infection.add(next_node)
                    visited[next_node] = True
                    q.append(next_node)
        
        answer = max(answer, len(cur_infection))
            
                
                
            

            
            
            
            

    
    
    return answer