from itertools import product
import copy
def solution(n, info):
    answer = []
    cases = []
    arr = []
    
    for i in range(11):
        arr.append((info[i] + 1, 0))
    
    # 경우의 수 모두 생성, 이기거나(1점 차이) 지는 것(0점)만 간주  (총 2^10개의 케이스)
    # 만약 화살 수가 남으면 빈 과녁에 몰아쏘기, 화살 수가 부족하면 case에 추가 X
    def make_cases(case, idx):
        if idx == 10:
            if sum(case) > n:
                return
            else:
                case.append(n - sum(case))
                cases.append(case)
                return
        
        for i in range(2):
            new_case = copy.deepcopy(case)
            new_case.append(arr[idx][i])
            make_cases(new_case, idx + 1)
            
    # 경우의 수 모두 생성
    make_cases([], 0)
    max_result = 0
    max_cases = []
    for case in cases:
        result = 0
        for i in range(10):
            if case[i] > info[i]:
                result = result + (10 - i)
            elif case[i] < info[i]:
                result = result - (10 - i)
        if result <= 0:
            continue
        reversed_string = ("".join(map(str, case)))[::-1]
        if result == max_result:
            max_cases.append(int(reversed_string))
        elif result > max_result:
            max_result = result
            max_cases = [int(reversed_string)]
        
    max_cases.sort()
    
    if not max_cases:
        return [-1]
    else:
        string = str(max_cases[-1])[::-1]
        for c in string:
            answer.append(int(c))
        while len(answer) < 11:
            answer.append(0)
        return answer