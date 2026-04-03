import sys
input = sys.stdin.readline

n, s = map(int, input().split())
x = list(map(int, input().split()))
h = list(map(int, input().split()))

s -= 1  # 0-index

low = high = s
L = x[s] - h[s]
R = x[s] + h[s]

while True:
    newL = L
    newR = R
    changed = False

    # 왼쪽으로 확장
    i = low - 1
    while i >= 0 and x[i] >= L:
        low = i
        newL = min(newL, x[i] - h[i])
        newR = max(newR, x[i] + h[i])
        changed = True
        i -= 1

    # 오른쪽으로 확장
    i = high + 1
    while i < n and x[i] <= R:
        high = i
        newL = min(newL, x[i] - h[i])
        newR = max(newR, x[i] + h[i])
        changed = True
        i += 1

    if not changed and newL == L and newR == R:
        break

    if newL == L and newR == R:
        break

    L, R = newL, newR

print(*range(low + 1, high + 2))