import sys


T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())

    answer = 1

    for i in range(M,M-N,-1):
        answer *= i

    for j in range(1,N+1):
        answer //= j


    print(answer)