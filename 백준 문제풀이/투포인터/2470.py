import sys


N = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

start = 0
end = N-1


answer = 1e10
result = []
while start < end:
    sum = arr[start] + arr[end]

    if abs(sum) < answer:
        answer = abs(sum)
        result = [arr[start], arr[end]]

    if sum > 0:
        end -= 1
    else:
        start += 1
    
print(result[0], result[1])