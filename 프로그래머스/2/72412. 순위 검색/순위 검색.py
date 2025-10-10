from collections import defaultdict
import copy
import sys
def solution(info, query):
    answer = []
    total_num = 0
    # taret 이상의 값을 갖는 인덱스 반환하는 함수
    def binary_search(arr, left, right, target):
        answer = right + 1
        while left <= right:
            middle = (left + right) // 2
            
            if arr[middle] >= target:
                answer = middle
                right = middle - 1
                continue
            else:
                left = middle + 1
                
        return answer
    def insert_items(insert_list, target_list, score, count):
        if count == 4:
            info_dict[tuple(target_list)].append(int(score))
            return
        for i in range(2):
            new_list = copy.deepcopy(target_list)
            new_list.append(insert_list[count][i])
            insert_items(insert_list, new_list, score, count + 1)
    
    info_dict = defaultdict(list)
    for i in info:
        lang, major, experience, food, score = i.split(" ")
        insert_list = [(lang, "-"), (major, "-"), (experience, "-"), (food, "-")]
        insert_items(insert_list, [], int(score), 0)
    
    # 모든 키값에 해당하는 리스트 정렬
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for q in query:
        q = q.replace(" and ", " ")
        lang, major, experience, food, score = q.split(" ")
        arr = info_dict[(lang,major,experience,food)]
        N = len(arr)
        idx = binary_search(arr ,0, N-1, int(score))
        answer.append(N-idx)
    return answer