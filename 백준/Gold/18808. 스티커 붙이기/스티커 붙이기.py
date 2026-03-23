import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

board = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    R,C = map(int, sys.stdin.readline().strip().split())

    sticker = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

    stickers.append(sticker)


def rotate_sticker(sticker):

    R = len(sticker)
    C = len(sticker[0])

    rotated_sticker = [[0] * R for _ in range(C)]
    
    for i in range(R):
        for j in range(C):
            rotated_sticker[j][R-1-i] = sticker[i][j]

    return rotated_sticker

def check_sticker(board, sticker, start_pos):
    start_r, start_c = start_pos
    temp_sticker = []
    for r in range(len(sticker)):
        for c in range(len(sticker[0])):
            if sticker[r][c] == 0:
                continue
            if sticker[r][c] == board[start_r + r][start_c + c]:
                return False
            temp_sticker.append((start_r + r, start_c + c))
    
    for r,c in temp_sticker:
        board[r][c] = 1

    return True
            
    

for idx in range(K):
    
    sticker = stickers[idx]
    for i in range(4):
        isSuccess = False 

        if i != 0:
            sticker = rotate_sticker(sticker)

        
        for j in range(N+1-len(sticker)):
            if (isSuccess):
                break

            for k in range(M+1-len(sticker[0])):
                result = check_sticker(board, sticker, (j,k))
                if result:
                    isSuccess = True
                    break
        
        if (isSuccess):
            break
    
counter = 0
for row in board:
    for val in row:
        if val == 1:
            counter += 1
print(counter)        
        
