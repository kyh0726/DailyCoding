def solution(play_time, adv_time, logs):
    answer = ''
    
    def convert_log_to_sec(string):
        hrs, mins, secs = map(int, string.split(':'))
        return hrs * 3600 + mins * 60 + secs
    
    def convert_sec_to_log(number):
        hrs = number // 3600
        mins = (number % 3600) // 60
        sec = number % 60
        return str(hrs).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(sec).zfill(2)
    
    
    acc_sum = [0] * convert_log_to_sec("100:00:01")

    for log in logs:
        start_time, end_time = log.split("-")
        
        start_time_num = (convert_log_to_sec(start_time))
        end_time_num = (convert_log_to_sec(end_time))
        
        acc_sum[start_time_num] += 1
        acc_sum[end_time_num] -= 1
        
    adv_len = convert_log_to_sec(adv_time)
    
    
    max_length = 0
    cur_length = 0
    max_time = convert_sec_to_log(0)
    left_idx = 0
    left_acc_sum = 0
    right_idx = adv_len
    right_acc_sum = 0
    
    # 일단 초반 00 ~ advtime 을 기준으로 잡기
    for i in range(adv_len):
        right_acc_sum += acc_sum[i]
        cur_length += right_acc_sum
    
    max_length = cur_length
    
    N = len(acc_sum)
    while right_idx < N:
        # 최대 광고 시청 갱신할 경우
        if cur_length > max_length:
            max_length = cur_length
            max_time = convert_sec_to_log(left_idx)
        
        # 새로 들어오는 사람들 더해주기
        right_acc_sum += acc_sum[right_idx]
        right_idx += 1
        cur_length += right_acc_sum
        
        # 빠져나가는 사람들 처리해주기
        left_acc_sum += acc_sum[left_idx]
        left_idx += 1
        cur_length -= left_acc_sum
        
        
        
    
    
    
    return max_time