import sys
import heapq
R, C, M = map(int, sys.stdin.readline().strip().split())

maps = [[[] for _ in range(C+1)] for _ in range(R+1)]
dirs = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]

for i in range(M):
    r,c,s,d,z = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(maps[r][c], (z, s, d))

def move_shark(r,c,z,s,d):
    if d == 3 or d == 4:
        left_s = s % ( 2 * (C-1))
        while left_s > 0:
            c = c + left_s * dirs[d][1]
            if c > C:
                left_s = c - (C)
                c = C
                d = 4
            elif c < 1:
                left_s = 1 - (c)
                c = 1
                d = 3
            else:
                break
        return (r,c,z,s,d)
    


    elif d == 1 or d == 2:
        left_s = s % ( 2 * (R-1))
        while left_s > 0:
            r = r + left_s * dirs[d][0]
            if r > R:
                left_s = r - (R)
                r = R
                d = 1
            elif r < 1:
                left_s = 1 - r
                r = 1
                d = 2
            else:
                break
        return (r,c,z,s,d)

answer = 0 
for i in range(1, C+1):
    
    # 상어 건지기
    for j in range(1, R+1):
        if maps[j][i]:
            z,s,d = heapq.heappop(maps[j][i])
            answer += z 
            break
        if j == R:
            break

    shark_queue = []
    for r in range(1, R+1):
        for c in range(1, C+1):
            # 상어 찾아서 큐에 넣어
            if maps[r][c]:
                z,s,d = heapq.heappop(maps[r][c])
                shark_queue.append((r,c,z,s,d))
            
    while shark_queue:
        # 이동 시켜
        r,c,z,s,d = shark_queue.pop()
        (next_r, next_c, next_z, next_s, next_d) = move_shark(r,c,z,s,d)
        heapq.heappush(maps[next_r][next_c], (next_z,next_s,next_d))

    # 이동 마친후에 잡아먹어
    for r in range(1, R+1):
        for c in range(1, C+1):
            while maps[r][c] and len(maps[r][c]) > 1:
                heapq.heappop(maps[r][c])

    for idx, row in enumerate(maps):
        if idx == 0:
            continue
print(answer)