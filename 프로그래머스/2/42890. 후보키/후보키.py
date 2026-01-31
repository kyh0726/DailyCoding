from itertools import combinations
def solution(relation):
    answer = 0
    answer_list = []
    arr = []
    keys = []
    total_len = len(relation)
    for i in range(len(relation[0])):
        arr.append(i)
    
    # 모든 조합 케이스 구하기
    for i in range(1, len(relation[0]) + 1):
        keys.extend(list(map(list, combinations(arr, i))))
    
    
    
    for key_list in keys:
        total_set = set()
        
        for row in relation:
            temp = ""
            
            for key in key_list:
                temp += str(row[key])
            
            total_set.add(temp)
        
        if len(total_set) != total_len:
            continue
        isAllClear = True
        
        for temp_set in answer_list:
            count = 0
            for val in temp_set:
                if val in key_list:
                    count += 1
            if len(temp_set) == count:
                isAllClear = False
                
        if not isAllClear:
            continue
        answer_list.append(key_list)
        
        
    
    return len(answer_list)