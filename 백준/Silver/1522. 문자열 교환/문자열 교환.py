s = input().strip()
n = len(s)

a_count = s.count('a')

# a가 0개이거나 전체가 a면 교환 필요 없음
if a_count == 0 or a_count == n:
    print(0)
else:
    doubled = s + s

    # 첫 윈도우의 b 개수
    b_count = doubled[:a_count].count('b')
    answer = b_count

    # 길이 a_count인 윈도우를 한 칸씩 이동
    for i in range(1, n):
        if doubled[i - 1] == 'b':
            b_count -= 1
        if doubled[i + a_count - 1] == 'b':
            b_count += 1
        answer = min(answer, b_count)

    print(answer)