def solution(numbers):
    answer = ''
    
    string_numbers = sorted(list(map(str, numbers)),key=lambda x:x*4, reverse = True)
    
    for val in string_numbers:
        answer += val
    
    while len(answer) >= 2 and answer[0] == "0":
        answer = answer[1:]
    
    return answer