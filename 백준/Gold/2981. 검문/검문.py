import sys
import math


N = int(sys.stdin.readline().strip())
number_list = []
for i in range(N):
    number_list.append(int(sys.stdin.readline().strip()))

number_list.sort()

res_gcd = number_list[1] - number_list[0]

for i in range(1, N-1):
    res_gcd = math.gcd(res_gcd, number_list[i+1] - number_list[i])



result_list = []
for i in range(2, int(math.sqrt(res_gcd))+ 1):
    if res_gcd % i == 0:
        result_list.append(i)
        result_list.append(res_gcd // i)

result_list.sort()
result_list.append(res_gcd)

result_list = set(result_list)

print(*result_list)
