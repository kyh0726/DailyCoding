import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

tree = defaultdict(list)

for i in range(N):
    info = list(sys.stdin.readline().strip().split())

    cur = tree
    for food in info[1:]:
        if food not in cur:
            cur[food] = {}
        cur = cur[food]



def print_numbers(node, level):

    for key in sorted(node.keys()):
        print("--"*(level), end="")
        print(key)
        print_numbers(node[key], level + 1)


print_numbers(tree, 0)

