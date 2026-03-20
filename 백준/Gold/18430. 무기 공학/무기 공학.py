import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

max_count = 0

moves = [[(0,0), (1,0), (0,1)], [(0,1),(0,0),(1,1)], [(1,1),(0,1),(1,0)], [(1,0), (1,1), (0,0)]]


visited = [[False] * M for _ in range(N)]
def dfs(start, count):
    global max_count
    max_count = max(count, max_count)
    
    for idx in range(start, (N-1) * (M-1)):
        r = idx // (M-1)
        c = idx % (M-1)

        for k in range(4):
            temp = moves[k]

            is_visited = False

            for dr, dc in temp:
                if visited[r + dr][c + dc]:
                    is_visited = True
                    break

            if is_visited:
                continue
            else:
                temp_count = 0
                for i in range(3):
                    dr, dc = temp[i]
                    next_r, next_c = r + dr, c + dc
                    visited[next_r][next_c] = True
                    if i == 0:
                        temp_count += board[next_r][next_c] * 2
                    else:
                        temp_count += board[next_r][next_c]
                    
                dfs(idx, count + temp_count)

                for i in range(3):
                    dr, dc = temp[i]
                    next_r, next_c = r + dr, c + dc
                    visited[next_r][next_c] = False






dfs(0,0)
print(max_count)
            




