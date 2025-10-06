def solution(n, arr1, arr2):
    answer = []
    target = 20
    
    def convert_to_binary(num):
        temp = num
        result = ""
        for i in range(n):
            remains = temp % 2
            temp = temp // 2
            if remains:
                result += "#"
            else:
                result += " "
        return result[::-1]
    
    for i in range(n):
        a_result = convert_to_binary(arr1[i])
        b_result = convert_to_binary(arr2[i])
        
        result = ""
        for j in range(n):
            if a_result[j] == " " and b_result[j] == " ":
                result += " "
            else:
                result += "#"
        
        answer.append(result)
                
        
    return answer