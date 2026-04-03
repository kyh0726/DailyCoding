import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

string = list(sys.stdin.readline().strip())
dicts = defaultdict(int)
counts = {"T":0, "G":0, "F":0, "P":0}

result = 0
dicts[(0,0,0,0)] = 1
for c in string:
    
    counts[c] += 1

    new_state = (
        counts["T"] % 3,
        counts["G"] % 3,
        counts["F"] % 3,
        counts["P"] % 3,
    )

    result += dicts[new_state]
    dicts[new_state] += 1

print(result)