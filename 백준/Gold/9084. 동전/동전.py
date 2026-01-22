import sys

T = int(sys.stdin.readline().strip())
result = []
for i in range(T):
    N = int(sys.stdin.readline().strip())
    coin_list = list(map(int, sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())

    coin_cases = [1] + [0] * (target)

    for coin in coin_list:
        for i in range(coin, target + 1):
            coin_cases[i] = coin_cases[i] + coin_cases[i-coin]

    print(coin_cases[target])


