import sys
from collections import deque

N = int(sys.stdin.readline().strip())
answer = set()
right_line = [False] * (2*N - 1)
left_line = [False] * (2*N - 1)
vertical_line = [False] * (N + 1)

count = 0




def bfs(k):
    global count
    if k == N + 1:
        count += 1

    for i in range(1, N+1): # k가 행, i가 열열
        if not vertical_line[i] and not right_line[i+k - 2] and not left_line[N-1 + (i - k)]:
            vertical_line[i] = True
            right_line[i+k - 2] = True
            left_line[N-1 + (i - k)] = True
            bfs(k + 1)
            vertical_line[i] = False
            right_line[i+k - 2] = False
            left_line[N-1 + (i - k)] = False
            
bfs(1)
print(count)
