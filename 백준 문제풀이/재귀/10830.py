import sys

N, B = map(int, sys.stdin.readline().strip().split())

A = [[0] * N for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().strip().split()))

# U와 V의 내적
def mul(U, V): 
    n = len(U)
    Z = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            e = 0
            for i in range(N):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000
    return Z

# 재귀적으로 행렬 연산 수행
def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)

    # 홀수면 곱한 결과에서 A를 한번 더 곱함
    if B % 2: 
        return mul(mul(tmp,tmp), A)
    # 짝수면 그대로 tmp, tmp 곱해서 return
    else:
        return mul(tmp,tmp)
    
result = square(A,B)
for r in result:
    print(*r)
