import sys
from collections import deque
import copy
N = int(sys.stdin.readline().strip())

board = [list(map(str, sys.stdin.readline().strip().split())) for _ in range(N)]

moves = [(0,1), (0,-1), (1,0), (-1,0)]
def put_objects():
    q = deque()
    result = []
    q.append([])

    while q:
        cur_list = q.popleft()

        if len(cur_list) == 3:
            result.append(cur_list)
            continue

        for i in range(N):
            for j in range(N):
                if board[i][j] == "S" or board[i][j] == "T" or (i,j) in cur_list:
                    continue
                copy_list = copy.deepcopy(cur_list)
                copy_list.append((i,j))
                q.append(copy_list)
    return result

def check_safety(cur_pos, objects):
    r,c = cur_pos
    for dr,dc in moves:
        idx = 1

        while 0 <= r + dr * idx < N and 0 <= c + dc * idx < N:
            if board[r + dr * idx][c + dc * idx] == "T":
                return False
            if (r + dr * idx, c + dc * idx) in objects:
                break
            idx += 1
    return True


        
        
    


cases = put_objects()


for case in cases:
    isFail = False
    for i in range(N): 
        for j in range(N):
            if board[i][j] == "S" and not check_safety((i,j), case):
                isFail = True

    if not isFail:
        print("YES")
        exit(0)

print("NO")