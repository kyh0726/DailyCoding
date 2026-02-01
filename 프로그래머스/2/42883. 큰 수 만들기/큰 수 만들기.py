def solution(number, k):
    answer = ''
    stack = []
    pop_num = 0
    for num in number:
        
        while stack and pop_num < k and stack[-1] < num:
            stack.pop()
            pop_num += 1
        
        stack.append(num)
    
    for i in range (k - pop_num):
        stack.pop()
        
    
    for val in stack:
        answer += val
        
    
    return answer