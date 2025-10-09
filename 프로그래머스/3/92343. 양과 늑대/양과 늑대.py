from collections import defaultdict
answer = 0
def solution(info, edges):
    visited = [False] * (len(info))
    visited[0] = True
    
    def dfs(sheeps, wolves):
        global answer
        answer = max(sheeps, answer)    
        for p_node, c_node in edges:
            if visited[p_node] and not visited[c_node]:
                visited[c_node] = True
                if info[c_node] == 0:
                    dfs(sheeps + 1, wolves)
                else:
                    if sheeps > wolves + 1:
                        dfs(sheeps, wolves + 1)
                
                visited[c_node] = False

        
    dfs(1,0)
    
    
    return answer