import copy
def solution(n, q, ans):
    answer = 0
    cases = []
    
    
    def make_cases(case):
        
        if len(case) == 5:
            cases.append(set(case))
            return
        
        for i in range(1,n+1):
            if not case or i < case[-1]:
                temp = copy.deepcopy(case)
                temp.append(i)
                make_cases(temp)
    
    make_cases([])
    
    for case in cases:
        q_len = len(q)
        isFail = False
        
        for i in range(q_len):
            target_idx = ans[i]
            
            count = 0
            for val in q[i]:
                if val in case:
                    count += 1
            
            if count != target_idx:
                isFail = True
                break
        
        if not isFail:
            answer += 1
            
            
            
            
        
        
        
        
        
        
    return answer