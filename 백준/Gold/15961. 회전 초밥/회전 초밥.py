import sys
from collections import defaultdict, deque

N, d, k, c = map(int, sys.stdin.readline().strip().split())

dishes = defaultdict(int)
belts = [int(sys.stdin.readline().strip()) for i in range(N)]
result = 0
q = deque()

def add_dish(dish):
    if dish == c:
        return 0


    dishes[dish] += 1
    
    if dishes[dish] > 1:
        return 0
    
    return 1

def delete_dish(dish):
    if dish == c:
        return 0
    
    dishes[dish] -= 1

    if dishes[dish] == 0:
        return 1
    
    return 0


total = 0
for i in range(k):
    q.append(belts[i])
    total += add_dish(belts[i])
    result = max(total, result)


for i in range(k, N+k):
    pop_val = q.popleft()
    add_val = belts[(i)%N]
    q.append(add_val)

    total += add_dish(add_val)
    total -= delete_dish(pop_val)

    result = max(total, result)


print(result + 1)