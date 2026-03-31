import sys, copy
from collections import defaultdict, deque

numbers = list(map(int,sys.stdin.readline().strip().split()))
graph = defaultdict(list)

def get_point(target):
    if target >= 100:
        return target // 10
    else:
        return target

def make_board():
    ways = [[0,2,4,6,8,10,12,14,161,18,20,221,241,261,281,301,32,34,36,38,40], [10,13,162,19,25,302,35,40], [20,222,242,25,302,35,40], [301,282,27,262,25,302,35,40]]
    
    for way in ways:
        for j in range(len(way)):
            idx = 1
            if len(way) == len(ways[0]) and way[j] in [10,20,301]:
                continue
            
            if len(graph[way[j]]) > 0:
                continue

            while j + idx < len(way) and idx <= 5:
                graph[way[j]].append(way[j+idx])
                idx += 1



make_board()


start = [[0,0,0,0], 0, 0]
q = deque()
q.append(start)
visited = defaultdict(int)
max_count = 0
while q:
    horses, count, point = q.popleft()


    if count == len(numbers):
        max_count = max(point, max_count)
        continue

    for i in range(4):
        copy_horses = copy.deepcopy(horses)
        cur_pos = copy_horses[i]
        cur_move_count = numbers[count]
        if cur_pos == -1:
            continue
        
        if len(graph[cur_pos]) < cur_move_count:
            copy_horses[i] = -1
            q.append((copy_horses, count + 1, point))
            continue

        next_pos = graph[cur_pos][cur_move_count-1]
        if next_pos in copy_horses:
            continue
        next_point = point + get_point(next_pos)
        copy_horses[i] = next_pos

        q.append((copy_horses, count + 1, next_point))

        
        

print(max_count)