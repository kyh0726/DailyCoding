import sys

N, M = map(int, sys.stdin.readline().strip().split())
courses = list(map(int, sys.stdin.readline().strip().split()))
answer = 0
start = max(courses)
end = sum(courses)

while start <= end:
  mid = ( start + end ) // 2
  total = 0
  count = 1

  for T in courses:
    if total + T > mid:
      count += 1
      total = 0
    total += T

  if count <= M:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1


print(answer)