import sys
from itertools import combinations

N, K = map(int,sys.stdin.readline().strip().split())

arr = []
string_list = []
dp = []

for i in range(N):
  s = sys.stdin.readline().strip()
  string_list.append(s[4:-4])

  
for i in range(ord('a'), ord('z') + 1):
  if i in [ord('a'), ord('n'), ord('t'), ord('i'), ord('c')]:
    continue
  arr.append(chr(i))
if K < 5:
  print(0)
  exit(0)


combs = list(combinations(arr,K-5))
max_answer = 0

fixed_arr= ['a','n','t','i','c']
for comb in combs:
  answer = 0
  for string in string_list:
    if string == '':
      answer += 1
    for idx,c in enumerate(string):

      if c not in comb and c not in fixed_arr:
        break
      if idx == len(string) - 1:
        answer += 1

    
  max_answer = max(answer, max_answer)

print(max_answer)