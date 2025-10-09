def solution(s):
    answer = 0
    l = len(s)
    min_string = l
    for i in range(1, l // 2 + 1):
        # i = chunk 기준
        tokens = []
        idx = 0
        while idx + i <= len(s):
            tokens.append(s[idx:idx+i])
            idx += i
            
        last_token = tokens[0]
        delete_sum = 0
        can_delete_num = 0
        for j in range(1, len(tokens)):
            if tokens[j] == last_token:
                can_delete_num += 1
                if j == len(tokens) - 1:
                    delete_sum += (can_delete_num * i - 1)
                    if can_delete_num + 1 >= 1000:
                        delete_sum -= 3
                    elif can_delete_num + 1 >= 100:
                        delete_sum -= 2
                    elif can_delete_num + 1 >= 10:
                        delete_sum -= 1
            else:
                if can_delete_num > 0:
                    delete_sum += (can_delete_num * i - 1)
                    if can_delete_num + 1 >= 1000:
                        delete_sum -= 3
                    elif can_delete_num + 1 >= 100:
                        delete_sum -= 2
                    elif can_delete_num + 1 >= 10:
                        delete_sum -= 1
                can_delete_num = 0
                last_token = tokens[j]
        min_string = min(min_string, l - delete_sum)
        
            
            
            
    
    return min_string