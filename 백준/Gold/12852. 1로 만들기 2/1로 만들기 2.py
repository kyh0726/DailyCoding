import sys
from collections import deque
N = int(sys.stdin.readline().strip())

cases = ["+", "x2", "x3"]

arr = [-1] * (N + 1)

arr[1] = 0

if N == 1:
    print(0)
    print(1)
    exit(0)

q = deque()
q.append((1, [1]))
while q:
    pop_val, numbers = q.popleft()

    for case in cases:
        next_val = 0
        if case == "+":
            next_val = pop_val + 1
        elif case == "x2":
            next_val = pop_val * 2
        elif case == "x3":
            next_val = pop_val * 3

        if next_val > N:
            continue
        if next_val == N:
            print(arr[pop_val] + 1)
            numbers.append(next_val)
            numbers.reverse()
            print(' '.join(map(str, numbers)))
            

            exit(0)

        
        if arr[next_val] == -1 or arr[next_val] > arr[pop_val] + 1:
            new_arr = numbers.copy()
            new_arr.append(next_val)
            arr[next_val] = arr[pop_val] + 1
            q.append((next_val, new_arr))
        else:
            continue



