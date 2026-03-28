import sys
from collections import deque, defaultdict

total = 1


N = int(sys.stdin.readline().strip())

numbers_string = sys.stdin.readline().strip()
visited = defaultdict(bool)

numbers = []
for char in numbers_string:
    numbers.append(char)

if N == 1:
    print(int(numbers_string))
    exit(0)

q = deque()

q.append(numbers)

def calc_numbers(numbers):

    a,operator,b = numbers[0], numbers[1], numbers[2]

    a = int(a)
    b = int(b)

    if operator == "+":
        return str(a + b)
    
    if operator == "*":
        return str(a * b)
    
    if operator == "-":
        return str(a - b)


max_num = -1e10

while q:
    pop_numbers = q.popleft()

    if len(pop_numbers) == 1:
        max_num = max(max_num, int(pop_numbers[0]))
        continue


    count = len(pop_numbers) // 2

    
    for i in range(count):
        left = pop_numbers[:2*i]
        right = pop_numbers[2*(i+1)+1:]
        calculated_number = calc_numbers(pop_numbers[2*i:2*(i+1)+1])
        new_number = left + [calculated_number] + right

        if visited[tuple(new_number)]:
            continue
        visited[tuple(new_number)] = True
        q.append(new_number)







print(max_num)