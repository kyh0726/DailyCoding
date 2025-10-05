from collections import defaultdict
from itertools import permutations
import copy
def solution(expression):
    answer = 0
    oper_list = ["+", "-", "*"]
    operands = []
    operators = []
    idx = 0
    max_idx = len(expression) - 1
    oper_count = defaultdict(int)
    
    def calc(x,y,operator):
        if operator == "+":
            return int(x) + int(y)
        elif operator == "-":
            return int(x) - int(y)
        else:
            return x * y
    
    while idx <= max_idx:
        if expression[idx] in oper_list:
            operators.append(expression[idx])
            oper_count[expression[idx]] += 1
        idx += 1
    
    
    expression = expression.replace("+", ",").replace("-", ",").replace("*", ",")

    operands = list(map(int, expression.split(",")) )
    
    cases = list(permutations(oper_list, 3))

    
    for case in cases:
        temp_operands = copy.deepcopy(operands)
        temp_operators = copy.deepcopy(operators)
        
        for operator in case:
            target_num = oper_count[operator]
            for i in range(target_num):
                idx = 0
                while idx < len(temp_operators):
                    if temp_operators[idx] == operator:
                        temp_operators.pop(idx)
                        a_operand = temp_operands.pop(idx)
                        b_operand = temp_operands.pop(idx)
                        # 결과 도출 및 다시 삽입
                        result = calc(a_operand, b_operand, operator)
                        temp_operands.insert(idx, result)
                        break
                    idx += 1
            
        answer = max(answer, abs(temp_operands[0]))
        
    
    return answer