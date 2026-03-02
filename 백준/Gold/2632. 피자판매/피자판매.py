import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

A,B = map(int, sys.stdin.readline().strip().split())

pizzas = defaultdict(list)
pizzas_num = defaultdict(int)

for i in range(A):
    pizzas["A"].append(int(sys.stdin.readline().strip()))
for i in range(B):
    pizzas["B"].append(int(sys.stdin.readline().strip()))

for gap in range(1, A):
    total = 0
    for i in range(A):
        if i == 0:
            total = sum(pizzas["A"][:gap])
            pizzas_num[("A", total)] += 1
            continue
        total += pizzas["A"][(i+gap-1)%A]
        total -= pizzas["A"][(i-1)%A]
        pizzas_num[("A", total)] += 1
pizzas_num[("A", sum(pizzas["A"]))] += 1

for gap in range(1, B):
    total = 0
    for i in range(B):
        if i == 0:
            total = sum(pizzas["B"][:gap])
            pizzas_num[("B", total)] += 1
            continue
        total += pizzas["B"][(i+gap-1)%B]
        total -= pizzas["B"][(i-1)%B]
        pizzas_num[("B", total)] += 1
pizzas_num[("B", sum(pizzas["B"]))] += 1


result = 0
for i in range(1,N):
    result += pizzas_num[("A", i)] * pizzas_num[("B", N-i)]

result += pizzas_num[("A", N)] + pizzas_num[("B", N)]
print(result)