import sys
from collections import deque

N = int(sys.stdin.readline().strip())

arr = [10000000] * 1001

q = deque()
q.append((1,0))
arr[1] = 0
while q:
    idx, count = q.popleft()
    
    # 이전 인덱스로 이동하는게 비용이 더 낮을 경우 큐에 추가
    if 2 <= idx -1 and arr[idx - 1] > count + 1:
        arr[idx - 1] = count + 1
        q.append((idx - 1, count + 1))

    i = 2
    while idx * i <= 1000 and arr[idx * i] >= count + i:
        arr[idx * i] = count + i
        q.append((idx * i, count + i))
        i += 1

print(arr[N])