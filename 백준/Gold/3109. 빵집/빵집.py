import sys

R, C = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(R)]

moves = [(-1,1), (0,1), (1,1)]
count = 0

#     - (시간초과 예방) 단, 가장 위에서 파이프를 설치를 했으나 마지막 열에 도달 하지 못한 곳은
#       추후 파이프를 설치를 해도 도달하지 못하므로 설치한 파이프('o')를 원상복귀('.')하지 않아도 된다.



def move(r, c):
    global count
    board[r][c] = "x"
    if c == C-1:
        count += 1
        return True
    
    for dr, dc in moves:
        next_r, next_c = r + dr, c + dc
        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            continue
        if board[next_r][next_c] == ".":
            if move(next_r, next_c):
                return True

    return False
    


for i in range(R):
    move(i,0)


print(count)