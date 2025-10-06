def solution(m, n, board):
    answer = 0
    moves = [(1,0), (0,1), (1,1)]
    new_board = []
    for i in range(m):
        new_board.append(list(board[i]))
        
    board = new_board
    
    
    def find_upper_block(r, c):
        while r >= 0:
            if board[r][c] != " ":
                return (r,c)
            r -= 1
            
        return (-1,-1)
            
    
    while True:
        total_popped_list = []
        for r in range(m-1):
            for c in range(n-1):
                # 지워진 부분은 pass
                if board[r][c] == " ":
                    continue
                popped_list = [(r,c)]
                isFail = False
                for dr, dc in moves:
                    next_r, next_c = r + dr, c + dc
                    if board[r][c] == board[next_r][next_c]:
                        popped_list.append((next_r,next_c))
                if len(popped_list) == 4:
                    total_popped_list.extend(popped_list)
                    
        if not total_popped_list:
            break
        
        # 지워진 부분 체크
        for r,c in total_popped_list:
            board[r][c] = " "
        
        # 밑으로 쏟아지는 로직
        
        for i in range(n):
            start = m-1
            while start >= 0:
                if board[start][i] == " ":
                    r, c = find_upper_block(start - 1, i)
                    # 블록이 있다면 swap
                    if (r,c) != (-1,-1):
                        board[start][i], board[r][c] = board[r][c], board[start][i]
                    
                start -= 1
                
        
    for i in range(m):
        for j in range(n):
            if board[i][j] == " ":
                answer += 1
                
        
    return answer