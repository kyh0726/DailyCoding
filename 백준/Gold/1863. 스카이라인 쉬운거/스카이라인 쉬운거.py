import sys

N = int(sys.stdin.readline().strip())

positions = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
positions.sort(key= lambda x: x[0], reverse=True)
stack = []
count = 0
while positions:
    x, y = positions.pop()

    while stack and stack[-1] > y:
        stack.pop()
        count += 1

    if stack and stack[-1] == y:
        continue

    if y != 0:
        stack.append(y)
    

while stack:
    stack.pop()
    count += 1

print(count)