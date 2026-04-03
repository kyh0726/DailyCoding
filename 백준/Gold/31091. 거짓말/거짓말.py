import sys

N = int(sys.stdin.readline().strip())

people = list(map(int, sys.stdin.readline().strip().split()))

L = [0] * (N+1)
U = [0] * (N+1)


for person in people:
    if person < 0:
        L[-person] += 1
    elif person > 0:
        U[person] += 1
    else:
        L[-person] += 1
        U[person] += 1



LS = [0] * (N+1)
US = [0] * (N+1)

for i in range(1, N+1):
    LS[i] = LS[i-1] + L[i-1]

for i in range(N-1,-1,-1):
    US[i] = US[i+1] + U[i+1]

answer = []
for i in range(N+1):
    if US[i] + LS[i] == i:
        answer.append(i)

print(len(answer))
print(*answer)

