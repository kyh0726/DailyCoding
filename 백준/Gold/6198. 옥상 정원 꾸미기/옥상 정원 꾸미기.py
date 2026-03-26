import sys

N = int(sys.stdin.readline().strip())

buildings = []

for i in range(N):
    buildings.append(int(sys.stdin.readline().strip()))

buildings.reverse()
stack = []
count = 0

while buildings:
    pop_building = buildings.pop()

    while stack and stack[-1] <= pop_building:
        stack.pop()
        count += len(stack)

    stack.append(pop_building)


while stack:
    stack.pop()
    count += len(stack)

print(count)
