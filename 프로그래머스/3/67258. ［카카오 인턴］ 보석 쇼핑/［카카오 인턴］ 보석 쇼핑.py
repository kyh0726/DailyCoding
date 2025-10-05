from collections import defaultdict
def solution(gems):
    answer = []
    max_gem_num = len(set(gems))
    gem_count = defaultdict(int)
    
    left = 0
    right = -1
    count = 0
    N = len(gems)
    min_set = [1,10000000000]
    
    while left < N and right < N:
        if count ==  max_gem_num:
            min_gap = min_set[1] - min_set[0]
            if right - left < min_gap:
                min_set = [left, right]
            elif right - left == min_gap and left < min_set[0]:
                min_set = [left, right]
                
            
        
        
        
        if count < max_gem_num:
            right += 1
            if right == N:
                break
            gem = gems[right]
            gem_count[gem] += 1
            if gem_count[gem] == 1:
                count += 1
        
        else:
            gem = gems[left]
            left += 1
            gem_count[gem] -= 1
            if gem_count[gem] == 0:
                count -= 1
        
        
        
    
        
    
    return [min_set[0] + 1, min_set[1] + 1]