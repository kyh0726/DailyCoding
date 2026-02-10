import sys

N = int(sys.stdin.readline().strip())
cows = []
for i in range(N):
    start_time, spending_time = map(int, sys.stdin.readline().strip().split())
    cows.append((start_time, spending_time))


cows.sort(key=lambda x:-x[0])


cur_time = 0

while cows:
    start_time, spending_time = cows.pop()

    if cur_time < start_time:
        cur_time = start_time

    cur_time += spending_time


print(cur_time)