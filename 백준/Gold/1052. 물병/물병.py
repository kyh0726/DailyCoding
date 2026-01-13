import sys

N, K = map(int, sys.stdin.readline().strip().split())


i = 0
while True:
    if list(bin(N + i)[2:]).count('1') <= K:
        print(i)
        exit(0)
    i += 1
