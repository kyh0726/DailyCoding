import sys
import heapq
from collections import defaultdict
N = int(sys.stdin.readline().strip())

max_heap = []
min_heap = []

P_to_L_mapper = defaultdict(int)
solved_problems = defaultdict(int)
for i in range(N):
    P, L = map(int, sys.stdin.readline().strip().split())
    P_to_L_mapper[P] = L
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    
M = int(sys.stdin.readline().strip())



def recommend_cmd(val):
    if val == -1:
        while solved_problems[min_heap[0][1]] > 0:
            solved_problems[min_heap[0][1]] -= 1
            heapq.heappop(min_heap)
        print(min_heap[0][1])
    if val == 1:
        while solved_problems[-max_heap[0][1]] > 0:
            solved_problems[-max_heap[0][1]] -= 1
            heapq.heappop(max_heap)
        print(-max_heap[0][1])

def add(P, L):
    P_to_L_mapper[P] = L
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))

def solved(P):
    solved_problems[P] += 1

for i in range(M):
    cmds = list(sys.stdin.readline().strip().split())


    if cmds[0] == "add":
        add(int(cmds[1]), int(cmds[2]))    

    if cmds[0] == "solved":
        solved(int(cmds[1]))
    
    if cmds[0] == "recommend":
        recommend_cmd(int(cmds[1]))