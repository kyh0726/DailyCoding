def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    acc_sum = [[0] * (M+1) for _ in range(N+1)]
    for cmd in skill:
        skill_type, start_r, start_c, end_r, end_c, amount = cmd
        if skill_type == 1:
            amount *= -1 
        acc_sum[start_r][start_c] += amount
        acc_sum[start_r][end_c + 1] -= amount
        acc_sum[end_r + 1][end_c + 1] += amount
        acc_sum[end_r + 1][start_c] -= amount
    
    
    for i in range(N):
        for j in range(1, M):
            acc_sum[i][j] += acc_sum[i][j-1]
            
    for i in range(1, N):
        for j in range(M):
            acc_sum[i][j] += acc_sum[i-1][j]
            
    for i in range(N):
        for j in range(M):
            if board[i][j] + acc_sum[i][j] >= 1:
                answer += 1
    
    return answer