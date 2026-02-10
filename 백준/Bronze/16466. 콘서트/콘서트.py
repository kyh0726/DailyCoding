import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

sold_nums = list(map(int, sys.stdin.readline().strip().split()))
sold_tickets = defaultdict(int)
for num in sold_nums:
    sold_tickets[num] = 1

num = 1
while True:
    if sold_tickets[num]:
        num += 1
        continue
    
    print(num)
    exit(0)