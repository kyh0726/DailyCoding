from collections import deque
def solution(storage, requests):
    answer = 0
    
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    R = len(storage)
    C = len(storage[0])
    
    board = [['@'] * (C+2)]
    
    for i in range(R):
        board.append(['@'] + list(storage[i]) + ['@'])
        
    board.append(['@'] * (C+2))
    
    def delete_all(target):
        for i in range(R+2):
            for j in range(C+2):
                if board[i][j] == target:
                    board[i][j] = '@'
    
    def delete_surface(target):
        q = deque()
        q.append((0,0))
        visited = [[False] * (C+2) for _ in range(R+2)]
        visited[0][0] = True
        
        to_delete_list = []
        while q:
            r, c = q.popleft()
            
            for dr, dc in moves:
                next_r, next_c = r + dr, c + dc
                
                if not ( 0 <= next_r < R+2 ) or not ( 0 <= next_c < C+2 ):
                    continue
                if visited[next_r][next_c]:
                    continue
                
                if board[next_r][next_c] == target:
                    visited[next_r][next_c] = True
                    to_delete_list.append((next_r, next_c))
                    continue
                if board[next_r][next_c] == "@":
                    visited[next_r][next_c] = True
                    q.append((next_r,next_c))
        
        for r,c in to_delete_list:
            board[r][c] = "@"
        

    for request in requests:
        if len(request) == 1:
            delete_surface(request)
        else:
            delete_all(request[0])
            
            
    for i in range(R+2):
        for j in range(C+2):
            if board[i][j] != "@":
                answer += 1
    
    return answer