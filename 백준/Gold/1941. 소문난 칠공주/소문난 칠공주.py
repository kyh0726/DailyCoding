import sys
from collections import deque

cases = []
moves = [(1,0),(-1,0),(0,1),(0,-1)]

board = [list(sys.stdin.readline().strip()) for _ in range(5)]

def make_cases(start, idx_lst):
    if len(idx_lst) == 7:
        cases.append((idx_lst[:]))
        return
        
    for i in range(start, 25):
        idx_lst.append((i//5, i%5))
        make_cases(i+1, idx_lst)
        idx_lst.pop()

def is_adjacent(arr):
    temp = arr[:]
    q = deque()
    q.append(temp.pop())
    arr_set = set(temp)

    while q:
        row, col = q.popleft()

        for dr, dc in moves:
            next_r, next_c = row+ dr, col + dc
            if (next_r,next_c) in arr_set:
                arr_set.remove((next_r,next_c))
                q.append((next_r,next_c))
    if arr_set:
        return False
    else:
        return True
        
def check_num(case):
    y_num = 0
    s_num = 0
    
    for row, col in case:
        if board[row][col] == "Y":
            y_num += 1
        else:
            s_num += 1
    if s_num >= 4:
        return True
    else:
        return False

make_cases(0, [])

result = 0
for case in cases:
    if not is_adjacent(case):
        continue
    if check_num(case):
        result += 1
print(result)
