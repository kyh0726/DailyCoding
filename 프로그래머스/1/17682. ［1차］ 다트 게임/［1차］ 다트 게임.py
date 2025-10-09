def solution(dartResult):
    answer = 0
    l = len(dartResult)
    num_list = []
    idx = 0
    while idx < l:
        # 숫자 추가
        if dartResult[idx:idx+2] == '10':
            num_list.append(10)
            idx += 2
        if '0' <= dartResult[idx] <= '9':
            num_list.append(int(dartResult[idx]))
            idx += 1
            
        
        # 제곱 처리 추가
        if dartResult[idx] == "D":
            num_list[-1] = num_list[-1] ** 2
        
        if dartResult[idx] == "T":
            num_list[-1] = num_list[-1] ** 3
        
        idx += 1
        
        
        while idx < l:
            if dartResult[idx] == "#":
                num_list[-1] *= -1
                idx += 1
            elif dartResult[idx] == "*":
                print(1243312, num_list)
                if len(num_list) > 1:
                    num_list[-1] *= 2
                    num_list[-2] *= 2
                else:
                    num_list[-1] *= 2
                idx += 1
            else:
                break
            
                
        
            
    
    return sum(num_list)