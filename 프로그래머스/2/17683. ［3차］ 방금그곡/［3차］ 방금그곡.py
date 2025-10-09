import heapq
def solution(m, musicinfos):
    answer_candidates = []
    def convert_time_to_number(time_string):
        hrs, mins = time_string.split(":")
        return 60 * int(hrs) + int(mins)
    #   B#은 시샾으로 도 네츄럴(C)랑 같습니다.
    #   E#은 미샾으로 미 네츄렬(F)랑 같습니다.


    def convert_music_form(string):
        result_string = ""
        lst = ["C","C#", "D", "D#", "E", "F", "F#" , "G", "G#", "A", "A#", "B"]
        dicts = {}
        for idx, val in enumerate(lst):
            dicts[val] = chr(ord('a') + idx)
        dicts["B#"] = "a"
        dicts["E#"] = "f"
        idx = 0
        l = len(string)
        
        while idx < l:
            if idx + 1 < l and dicts.get(string[idx:idx+2]):
                result_string += dicts[string[idx:idx+2]]
                idx += 2
            else:
                result_string += dicts[string[idx:idx+1]]
                idx +=1
        return result_string
        
    
    def compare_two_string(big_string, small_string, small_idx, remaining_time):
        if remaining_time < 0:
            return False
        time = 0
        big_idx = 0
        big_len = len(big_string)
        small_len = len(small_string)
        while big_idx < big_len and time < remaining_time:
            if big_string[big_idx] != small_string[small_idx]:
                return False
            small_idx = (small_idx + 1) % small_len
            big_idx += 1
            time += 1
            
        if big_idx == big_len:
            return True
        else:
            return False
    
    answer = ''
    m = convert_music_form(m)
    for idx, music_info in enumerate(musicinfos):
        start, end, title, content = music_info.split(',')
        content = convert_music_form(content)
        time_gap = convert_time_to_number(end) - convert_time_to_number(start)
        
        for i in range(len(content)):
            result = compare_two_string(m, content, i, time_gap - i)
            if result:
                heapq.heappush(answer_candidates, (-time_gap, idx, title))
                break
    if not answer_candidates:
        return "(None)"
    else:
        time_gap, idx, title = heapq.heappop(answer_candidates)
        return title                
