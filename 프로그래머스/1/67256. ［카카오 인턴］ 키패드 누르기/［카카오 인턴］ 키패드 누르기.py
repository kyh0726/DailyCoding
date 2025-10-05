def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    
    def get_position(number):
        if number == 0:
            return [3,1]
        return [(number-1 )// 3,(number - 1)% 3]
    
    def cal_distance(posA, posB):
        r_a, c_a = posA
        r_b, c_b = posB
        return abs(r_a-r_b) + abs(c_a-c_b)
    
    
    left_pos = [3,0]
    right_pos = [3,2]
    
    for number in numbers:
        next_pos = get_position(number)
        if number in left:
            answer += "L"
            left_pos = next_pos
            continue
        if number in right:
            answer += "R"
            right_pos = next_pos
            continue
        left_dis = cal_distance(left_pos, next_pos)
        right_dis = cal_distance(right_pos, next_pos)
        
        if left_dis == right_dis:
            if hand == 'right':
                right_pos = next_pos
                answer += "R"
                continue
            else:
                left_pos = next_pos
                answer += "L"
                continue
        
        if left_dis < right_dis:
            left_pos = next_pos
            answer += "L"
            continue
        if left_dis > right_dis:
            right_pos = next_pos
            answer += "R"
            continue
            
            
    return answer