def check_is_right(string):
        q = []
        idx = 0
        max_idx = len(string)
        while idx < max_idx:
            c = string[idx]
            if c == "(":
                q.append("(")
            else:
                if q and q[-1] == "(":
                    q.pop()
                else:
                    q.append("(")
            
            idx += 1
        
        # q에 남은 값 있는지 여부에 따라 참, 거짓 반환
        if q:
            return False
        else:
            return True

def split_string(string):
    if len(string) == 0:
        return string
    if check_is_right(string):
        return string

    left_num = 0
    right_num = 0
    idx = 0
    max_idx = len(string)
    while idx < max_idx:
        if string[idx] == "(":
            left_num += 1
        else:
            right_num += 1
        idx += 1
        if left_num == right_num:
            # u가 올바른 문자열이라면
            if check_is_right(string[:idx]):
                return string[:idx] + split_string(string[idx:max_idx])
            # u가 올바른 문자열이 아니라면
            else:
                return  "(" + split_string(string[idx:max_idx]) + ")" + reverse_string(string[:idx])
        
        
def reverse_string(string):
    middle_string = ""
    for c in string[1:-1]:
        if c == "(":
            middle_string += ")"
        else:
            middle_string += "("
    
    return  middle_string 
    
        
def solution(p):
    answer = ''
    return split_string(p)