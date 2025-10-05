from collections import deque, defaultdict
def solution(gems):
    answer = []
    min_val = 100001
    result = deque()
    gems = deque(gems)
    num = len(set(gems))
    collected_gems = set()
    num_count_dict = defaultdict(int)
    idx = 0
    while gems:
        
        # 만약 처음 result에 값을 넣는거라면 모든 종류의 gem이 들어가도록 result 값을 채워준다.
        if not result:
            while gems:
                idx += 1
                pop_val = gems.popleft()
                result.append(pop_val)
                collected_gems.add(pop_val)
                num_count_dict[pop_val] += 1
                if len(collected_gems) == num:
                    break
        else:
            idx += 1
            pop_val = gems.popleft()
        
            result.append(pop_val)
            num_count_dict[pop_val] += 1
        
        while result:
            if num_count_dict[result[0]] >= 2:
                num_count_dict[result[0]] -= 1
                result.popleft()
            else:
                break
        
        
        if len(result) < min_val:
            min_val = len(result)
            answer = [idx - len(result) + 1,idx]
        
        
    
    
    return answer