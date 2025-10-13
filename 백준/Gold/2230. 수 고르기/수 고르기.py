import sys



N, M = map(int, sys.stdin.readline().strip().split())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

answer = 1e10
arr.sort()

# target보다 가장 작은 큰 수를 찾는 binary_search
def binary_search(target, left, right):
    answer_idx = -1
    while left <= right:
        middle = (left + right) // 2

        if arr[middle] >= target:
            answer_idx = middle
            right = middle - 1
        else:
            left = middle + 1

    return answer_idx

            
            
        


for i in range(N-1):
    target = arr[i] + M
    target_idx = binary_search(target, i+1, N-1)
    if target_idx == -1:
        continue
    answer = min(answer, arr[target_idx] - arr[i])

print(answer)