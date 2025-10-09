import sys


N = int(sys.stdin.readline().strip())

k = int(sys.stdin.readline().strip())


start = 1
answer = 0
end = N*N

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for i in range(1, N+1):
        count += min(mid // i, N)
    
    if count >= k:
        answer = mid
        end = mid - 1

    else:
        start = mid + 1


print(answer)