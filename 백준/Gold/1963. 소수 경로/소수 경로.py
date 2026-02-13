import sys
from collections import deque

nums = [0] * 10000
nums[1] = 1
for i in range(2,100):
    for j in range(2,5000):
        if i*j >= 10000:
            continue
        nums[i*j] = 1


def bfs(start, target):
    visited = [False] * 10000
    q = deque()
    q.append((0,start))
    visited[int(start)] = True
    while q:
        count, pop_val = q.popleft()

        if pop_val == target:
            return count
        
        for i in range(4):
            for j in range(10):
                new_number = pop_val[:i] + str(j) + pop_val[i+1:]

                if visited[int(new_number)]:
                    continue
                if int(new_number) < 1000:
                    continue
                if nums[int(new_number)] == 1:
                    continue

                visited[int(new_number)] = True
                q.append((count + 1, new_number))


    return "Impossible"
        

    

    


N = int(sys.stdin.readline().strip())



for i in range(N):
    start, target = sys.stdin.readline().strip().split()

    result = bfs(start, target)

    print(result)







