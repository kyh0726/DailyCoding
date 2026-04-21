def solution(a):
    n = len(a)
    if n <= 2:
        return n

    answer = 2
    left_min = a[0]
    right_min = a[-1]

    for i in range(1, n - 1):
        if a[i] < left_min:
            left_min = a[i]
            answer += 1

        if a[n - 1 - i] < right_min:
            right_min = a[n - 1 - i]
            answer += 1

    if left_min == right_min:
        answer -= 1

    return answer