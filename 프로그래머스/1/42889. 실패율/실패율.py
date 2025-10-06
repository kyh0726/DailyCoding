from collections import defaultdict
def solution(N, stages):
    answer = []

    users_at_stage = defaultdict(int)
    users_num = len(stages)
    fail_rates = []
    for stage in stages:
        users_at_stage[stage] += 1

    list(set(stages)).sort()
    
    
    for i in range(1,N+1):
        if users_num == 0:
            fail_rates.append((i, 0))
            continue
        fail_rates.append((i, users_at_stage[i] / users_num))
        users_num -= users_at_stage[i]
    
    fail_rates.sort(key = lambda x: (-x[1], x[0]))
    
    for fail_rate in fail_rates:
        answer.append(fail_rate[0])
    
    return answer