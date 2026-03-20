import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
T = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 연산 개수
    commands = [sys.stdin.readline().strip() for _ in range(N)]  # N개 명령어 읽기
    max_heap = []
    min_heap = []
    exist = defaultdict(int)
    isExist = False
    for command in commands:
        action, val = command.split(' ')
        val = int(val)
        if action == "I":
            heappush(max_heap, -val)
            heappush(min_heap, val)
            exist[val] += 1

        else:
            if not min_heap or not max_heap:
                continue
            if val == 1:
                while max_heap and exist[-max_heap[0]] == 0:
                    heappop(max_heap)
                if max_heap and exist[-max_heap[0]] > 0:
                    pop_val = -heappop(max_heap)
                    exist[pop_val] -= 1

            if val == -1:
                while min_heap and exist[min_heap[0]] == 0:
                    heappop(min_heap)
                if min_heap and exist[min_heap[0]] > 0:
                    pop_val = heappop(min_heap)
                    exist[pop_val] -= 1

    while min_heap and exist[min_heap[0]] == 0:
        heappop(min_heap)
    while max_heap and exist[-max_heap[0]] == 0:
        heappop(max_heap)

    if min_heap and max_heap:
        print(f"{-max_heap[0]} {min_heap[0]}")  # 확인용 출력
    else:
        print('EMPTY')
