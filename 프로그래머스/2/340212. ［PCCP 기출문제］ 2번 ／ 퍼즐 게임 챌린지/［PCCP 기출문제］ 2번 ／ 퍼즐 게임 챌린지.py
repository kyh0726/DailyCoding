def solution(diffs, times, limit):
    
    # 퍼즐의 난이도 <= 레벨이면 현재 퍼즐의 소요시간
    # 퍼즐의 난이도 > 레벨이면 난이도 차이 횟수만큼 틀림 (틀릴 때마다 이전 퍼즐 소요시간(이전 퍼즐에서 틀렸던게 연쇄작용하지는 X) + 현재 퍼즐 소요시간 발생)
    # 이분탐색 접근
    
    def calc_time(level):
        N = len(diffs)
        total = 0
        for i in range(N):
            target_time = times[i]
            target_level = diffs[i]
            if level < target_level:
                total += (target_level - level + 1) * target_time + (target_level - level) * times[i-1]
            else:
                total += target_time
        
        return total
    
    def binary_search():
        answer = 0 
        left = 1
        right = max(diffs)
        while left <= right:
            middle = (left + right) // 2
            time = calc_time(middle)
            
            if time <= limit:
                answer = middle
                right = middle - 1
            else:   
                left = middle + 1
        return answer
            
        
        
        
    
    
    
    return binary_search()