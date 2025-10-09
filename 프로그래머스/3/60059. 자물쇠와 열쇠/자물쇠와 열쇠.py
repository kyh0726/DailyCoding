import copy
def solution(key, lock):
    answer = True
    N = len(lock)
    M = len(key)
    target_count = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                target_count += 1
    
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    keys = [key]
    board = []
    def make_cases(M):
        temp_board = copy.deepcopy(key)
        for _ in range(3):
            new_board = [[0] * M for _ in range(M)]
            for i in range(M):
                for j in range(M):
                    new_board[j][M-1-i] = temp_board[i][j]
            
            keys.append(new_board)
            temp_board = copy.deepcopy(new_board)
    make_cases(M)

    # 4방향 겉부분 모두 N-1 만큼의 껍질을 감싸줌
    for i in range(M-1):
        board.append([-1] * (N + 2 * (M-1)))
    for row in lock:
        board.append([-1] * (M-1) + row + [-1] * (M-1))
    for i in range(M-1):
        board.append([-1] * (N + 2 * (M-1)))
        
    
    for key in keys:
        for add_i in range(N + M - 1):
            for add_j in range(N + M - 1):
                count = 0
                isFalse = False
                for i in range(M):
                    for j in range(M):
                        board_i = i + add_i
                        board_j = j + add_j

                        if board[board_i][board_j] == -1:
                            continue
                        if board[board_i][board_j] + key[i][j] != 1:
                            isFalse = True
                        if board[board_i][board_j] == 0 and key[i][j] == 1:
                            count += 1
                if isFalse:
                    continue
                if count == target_count:
                    return True
                
                
        
    
    return False