import sys
from collections import defaultdict
T = int(sys.stdin.readline().strip())

for i in range(T):
    isEnd= False
    N = int(sys.stdin.readline().strip())
    dicts = defaultdict(int)
    numbers = []
    for j in range(N):
        numbers.append(sys.stdin.readline().strip())
    numbers.sort(reverse=True)

    for number in numbers:
        if dicts[number] == 1:
            isEnd=True
            break
        
        prefix = ''
        for c in number:
            prefix += c
            dicts[prefix] = 1


    if isEnd:
        print("NO")
    else:
        print("YES")