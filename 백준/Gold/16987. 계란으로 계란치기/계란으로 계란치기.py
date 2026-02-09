import sys


N = int(sys.stdin.readline().strip())

eggs = []
eggs.extend(list(map(int, sys.stdin.readline().strip().split())) for _ in range(N))
result = 0

def dfs(cur_idx, eggs):
    
    global result
    global N
    if cur_idx == N:
        broken_eggs = 0
        for egg in eggs:
            if egg[0] <= 0:
                broken_eggs += 1

        result = max(result, broken_eggs)
        return

    cur_egg_s, cur_egg_w = eggs[cur_idx]


    # 이미 깨진 계란
    if cur_egg_s <= 0:
        dfs(cur_idx + 1, eggs)
        return



    isBroken = True
    for next_idx in range(N):
        next_egg_s, next_egg_w = eggs[next_idx]
        
        if next_idx == cur_idx:
            continue
        if next_egg_s <= 0:
            continue
        isBroken = False
        eggs[cur_idx] = [cur_egg_s - next_egg_w, cur_egg_w]
        eggs[next_idx] = [next_egg_s - cur_egg_w, next_egg_w]

        dfs(cur_idx+1, eggs)

        eggs[cur_idx] = [cur_egg_s, cur_egg_w]
        eggs[next_idx] = [next_egg_s, next_egg_w]

    if isBroken:
        dfs(N, eggs)

dfs(0, eggs)
print(result)