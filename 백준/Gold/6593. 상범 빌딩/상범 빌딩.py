import sys
from collections import deque


while True:
    L, R, C = map(int, sys.stdin.readline().strip().split())
    if (L,R,C) == (0,0,0):
        exit(0)
    start = (0,0,0)
    end = (0,0,0)
    building = []
    moves = [(1,0,0), (-1,0,0), (0,1,0),(0,-1,0), (0,0,1),(0,0,-1)]
    
    def bfs(start):
        visited = [[[False] * C for _ in range(R)] for _ in range(L)]
        q = deque()
        q.append((start[0], start[1], start[2], 0))
        visited[start[0]][start[1]][start[2]] = True

        while q:
            l,r,c,count = q.popleft()

            if building[l][r][c] == "E": 
                return count

            for i in range(6):
                dl, dr, dc = moves[i]
                next_l, next_r, next_c = l + dl, r + dr, c + dc

                if next_l >= L or next_r >= R or next_c >= C or next_l < 0 or next_r < 0 or next_c < 0:
                    continue
                if visited[next_l][next_r][next_c]:
                    continue
                if building[next_l][next_r][next_c] == "#":
                    continue
                
                visited[next_l][next_r][next_c] = True
                q.append((next_l, next_r, next_c, count + 1))
        
        return 0

        

    for i in range(L):
        building.append([list(sys.stdin.readline().strip()) for _ in range(R)])
        sys.stdin.readline().strip()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == "S":
                    start = (i,j,k)
                if building[i][j][k] == "E":
                    end = (i,j,k)

    answer = bfs(start)

    if answer > 0:
        print("Escaped in " + str(answer) + " minute(s).")
    else:
        print("Trapped!")