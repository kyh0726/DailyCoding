import sys
from collections import defaultdict, deque

num_mapper = {(0,0,0,1,0,0,0):0, (1,1,0,1,1,0,1):1, (0,1,0,0,0,1,0):2, (0,1,0,0,1,0,0):3, (1,0,0,0,1,0,1):4, (0,0,1,0,1,0,0):5, (0,0,1,0,0,0,0):6, (0,1,0,1,1,0,1):7, (0,0,0,0,0,0,0):8, (0,0,0,0,1,0,0):9}

code_mapper = {0:(0,0,0,1,0,0,0), 1:(1,1,0,1,1,0,1), 2:(0,1,0,0,0,1,0), 3:(0,1,0,0,1,0,0), 4:(1,0,0,0,1,0,1), 5:(0,0,1,0,1,0,0), 6:(0,0,1,0,0,0,0), 7:(0,1,0,1,1,0,1), 8:(0,0,0,0,0,0,0), 9:(0,0,0,0,1,0,0)}

distances = [[0]*10 for _ in range(10)]


N, K, P, X = sys.stdin.readline().strip().split()


for i in range(0,10):
    for j in range(i + 1, 10):
        a = code_mapper[i]
        b = code_mapper[j]

        distance = 0
        for idx in range(7):
            if a[idx] != b[idx]:
                distance += 1

        distances[i][j] = distance
        distances[j][i] = distance

start_num = ''

for i in range(int(K) - len(X)):
    start_num += '0'

start_num += X


result = 0
def bfs(start_num, K):
    global N
    global result
    q = deque()
    q.append((start_num, K, 0))
    while q:
        pop_num, left_count, cur_idx = q.popleft()



        if cur_idx >= len(pop_num):
            if 1 <= int(pop_num) <= int(N) and int(pop_num) != int(start_num):
                result += 1
            continue
        
        rest_left = pop_num[:cur_idx]
        rest_right = pop_num[cur_idx+1:]

        cur_num = int(pop_num[cur_idx])

        for i in range(10):
            
            distance = distances[i][cur_num]
            if left_count - distance >= 0:
                next_num = rest_left + str(i) + rest_right
                q.append((next_num, left_count - distance, cur_idx + 1))
    


bfs(start_num, int(P))
print(result)