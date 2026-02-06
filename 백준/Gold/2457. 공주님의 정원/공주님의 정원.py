import sys
import heapq
N = int(sys.stdin.readline().strip())

date_mapper = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def date_to_num(month, date):
    total = 0
    for i in range(1, month):
        total += date_mapper[i]
    
    return total + date

min_start = date_to_num(3, 1)
max_end = date_to_num(11, 30)
flowers = []

for i in range(N):
    start_month, start_date, end_month, end_date = map(int, sys.stdin.readline().strip().split())
    
    start = max(min_start, date_to_num(start_month, start_date))
    end = date_to_num(end_month, end_date)

    heapq.heappush(flowers, (start, end))

cur_time = min_start
count = 0
while True:

    if cur_time > max_end:
        print(count)
        exit(0)


    popped_nums = []
    # 남은 꽃 배열에 지금 끝나는 시간보다 더 빨리 피는 꽃이 있다면
    while flowers and flowers[0][0] <= cur_time:
        start, end = heapq.heappop(flowers)
        heapq.heappush(popped_nums, -end)
    

    if popped_nums:
        end_time = - heapq.heappop(popped_nums)
        cur_time = end_time
        count += 1
    else:
        print(0)
        exit(0)

    

    

    







