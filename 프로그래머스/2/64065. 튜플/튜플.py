def solution(s):
    answer = []
    lst = s[2:-2].split("},{")
    
    lst.sort(key = lambda x: len(x))
    
    for string in lst:
        vals = map(int, string.split(","))
        for val in vals:
            if val not in answer:
                answer.append(val)
    return answer