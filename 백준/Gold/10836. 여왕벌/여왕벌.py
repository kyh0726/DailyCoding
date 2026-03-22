import sys


M,N = map(int, sys.stdin.readline().strip().split())

board = [[1] * M for _ in range(M)]



for _ in range(N):
    increase_nums = list(map(int, sys.stdin.readline().strip().split()))

    idx = 0

    for row in range(M-1,-1,-1):
        while increase_nums[idx] == 0:
            idx += 1

        board[row][0] += idx
        increase_nums[idx] -= 1
    
    for col in range(1, M):
        while increase_nums[idx] == 0:
            idx += 1

        board[0][col] += idx
        increase_nums[idx] -= 1
    

for i in range(1,M):
    for j in range(1,M):
        board[i][j] = board[i-1][j]


for row in board:
    for val in row:
        print(val, end=" ")
    
    print('')