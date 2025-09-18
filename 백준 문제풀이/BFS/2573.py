import sys
N, M = map(int, sys.stdin.readline().strip().split())

maps = [list(map(int, sys.stdin.readline().strip().split()))for i in range(N)]
moves = [(0,1), (0,-1), (1,0), (-1,0)]

    
time = 0
while True:
    count = 0
    mark = []
    visited = [[False] * (M) for _ in range(N)]

    def count_around_ice(first_row, first_col):
        q = []
        q.append((first_row, first_col))
        while q:
            row, col = q.pop()
            if (visited[row][col]):
                continue
            visited[row][col] = True
            minus = 0
            for dr, dc in moves:
                next_r, next_c = row + dr, col + dc
                if 0 <= next_r < N and 0 <= next_c < M:
                    if maps[next_r][next_c] != 0 and not visited[next_r][next_c]:
                        q.append((next_r,next_c))
                    if maps[next_r][next_c] == 0:
                        minus += 1
            mark.append((row,col,minus))

                    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0 and not visited[i][j]:
                count_around_ice(i,j)
                count += 1
    if count >= 2:
        print(time)
        break
    if count == 0:
        print(0)
        break

    time += 1


    for row,col,minus in mark:
        maps[row][col] = max(maps[row][col] - minus, 0)



                
                





