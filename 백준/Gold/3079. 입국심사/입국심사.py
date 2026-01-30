import sys

N, M = map(int, sys.stdin.readline().strip().split())
times = []
for i in range(N):
    times.append(int(sys.stdin.readline().strip()))

left = 1
right = max(times) * M
def cal_sum(time):
    count = 0

    for val in times:
        count += int(time // val)
    
    if count < M:
        return False
    else:
        return True
    
answer = 0
while left <= right:
    middle = (right + left) // 2

    result = cal_sum(middle)

    if result:
        answer = middle
        right = middle - 1
    else:
        left = middle + 1

    

print(int(answer))