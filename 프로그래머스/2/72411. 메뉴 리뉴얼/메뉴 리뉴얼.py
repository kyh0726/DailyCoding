from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    combs = []
    max_count = defaultdict(int)
    max_list = defaultdict(list)
    course_count = defaultdict(int)
    for order in orders:
        N = len(order)
        order_list = sorted(list(order))
        for i in range(2,N+1):
            # 코스로 주어지는 경우에만
            if i in course:
                combs.append(list(combinations(order_list, i)))
    
    
    for comb in combs:
        for course_idx in comb:
            course_count[course_idx] += 1
            if course_count[course_idx] < 2:
                continue
            
        
            # course name 문자열로 변경
            course_name = ""
            for char in list(course_idx):
                course_name += char
            course_len = len(course_name)
            if course_count[course_idx] > max_count[course_len]:
                max_list[course_len] = []
                max_count[course_len] = course_count[course_idx]
        
                max_list[course_len].append(course_name)
            elif course_count[course_idx] == max_count[course_len]:                
                max_list[course_len].append(course_name)
    
    
    for key in max_list.keys():
        answer.extend(max_list[key])
        
    
    return sorted(answer)