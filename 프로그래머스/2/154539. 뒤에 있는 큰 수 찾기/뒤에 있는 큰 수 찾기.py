def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            pop_idx = stack.pop()
            result[pop_idx] = number
        
        stack.append(idx)
            
    
    return result
