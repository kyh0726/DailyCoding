def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries.reverse()
    pickups.reverse()
    

    def make_chunks(arr):
        chunked_arr = []
        idx = 0
        while idx < n:
            # 배달, 수거할 필요 없는 곳
            if arr[idx] == 0:
                idx += 1
                continue
            
            add_idx = 0
            current_capa = 0
            # 배달 수거 필요
            while idx + add_idx < n:
                target_idx = idx + add_idx
                # 담을 수 있으면 담고 다음으로 이동
                if arr[target_idx] + current_capa <= cap:
                    current_capa += arr[target_idx]
                    arr[target_idx] = 0
                    add_idx += 1
                # 못 담는 순간 담을 수 있을 만큼만 담고 break
                else:
                    arr[target_idx] -= (cap - current_capa)
                    current_capa = cap
                    break
            if current_capa > 0:
                chunked_arr.append(n-idx)
                idx += add_idx
            else:
                idx += add_idx
        return chunked_arr
                    
            
    
        
    chunked_d_list = make_chunks(deliveries)
    chunked_p_list = make_chunks(pickups)
    
    d_len = len(chunked_d_list)
    p_len = len(chunked_p_list)
    
    if d_len > p_len:
        for i in range(d_len - p_len):
            chunked_p_list.append(0)
    else:
        for i in range(p_len - d_len):
            chunked_d_list.append(0)
            
    for i in range(len(chunked_d_list)):
        answer += (2 * max(chunked_p_list[i], chunked_d_list[i]))
        
    return answer