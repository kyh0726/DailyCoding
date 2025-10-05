def solution(s):
    answer = ''
    num_string = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    print(s[0])
    while s:
        if ord('0') <= ord(s[0]) <= ord('9'):
            answer += s[0]
            s = s[1:]
            continue
            
        for idx, val in enumerate(num_string):
            if s.startswith(val):
                answer += str(idx)
                str_len = len(val)
                s = s[str_len:]
                break        
    return int(answer)  