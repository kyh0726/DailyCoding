import sys
from collections import defaultdict
N, M, K = map(int, sys.stdin.readline().strip().split())


dirs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
fires = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

for i in range(len(fires)):
    fires[i][0] -= 1
    fires[i][1] -= 1

def move(r,c,s,d):
    next_r = (r + dirs[d][0] * s) % N
    next_c = (c + dirs[d][1] * s) % N
    return (next_r, next_c)

def merge(lst):
    m = 0
    s = 0
    for dm, ds, _ in lst:
        m += dm
        s += ds

    m = m // 5
    s = s // len(lst)
    
    return (m,s)

def find_next_dir(lst):
    temp = []
    for _, __, dir in lst:
        temp.append(dir % 2)
    
    # 다 홀수 혹은 짝수
    if sum(temp) == 0 or sum(temp) == len(temp):
        return 0
    else:
        return 1

for i in range(K):
    temp_fires = defaultdict(list)

    while fires:
        r,c,m,s,d = fires.pop()
        next_r, next_c = move(r,c,s,d)
        temp_fires[(next_r, next_c)].append((m,s,d))
    
    keys = temp_fires.keys()
    for key in keys:
        value = temp_fires[key]
        if len(value) == 1:
            r,c = key
            m,s,d = value[0]
            fires.append((r,c,m,s,d))
        else:
            r, c = key
            m, s = merge(value) 
            next_dir = find_next_dir(value)

            if m == 0:
                continue
            else:
                for i in range(4):
                    fires.append((r,c,m,s,next_dir + i * 2))
    
sum = 0
for r,c,m,s,d in fires:
    sum += m
print(sum)