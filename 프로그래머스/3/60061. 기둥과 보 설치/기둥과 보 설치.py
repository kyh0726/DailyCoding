def solution(n, build_frame):
    # 기둥 세울 수 있는 곳 = 바닥 or 기존에 세워둔 기둥 위 or 보의 끝자락
    # 보 둘 수 있는 곳 = 기존에 세워둔 기둥 위 or 좌우에 보 미리 설치됨 ()
    frame_set = set()
    def check_is_okay():
        for x,y,a in frame_set:
            if a == 0:
                if check_is_col_okay(x,y):
                    continue
                return False
            else:
                if check_is_row_okay(x,y):
                    continue
                return False
        return True
            
    def check_is_col_okay(x,y):
        if (x,y-1,0) in frame_set or (x-1,y,1) in frame_set or (x,y,1) in frame_set or y == 0:
            return True
        return False
    
    def check_is_row_okay(x,y):
        if (x+1,y-1,0) in frame_set or (x,y-1,0) in frame_set or ((x-1,y,1) in frame_set and (x+1,y,1) in frame_set):
            return True
        return False
    
    check_func = [check_is_col_okay]
    
    for x,y,a,b in build_frame:
        if b == 1:
            if a == 0 and check_is_col_okay(x,y):
                frame_set.add((x,y,a))
            if a == 1 and check_is_row_okay(x,y):
                frame_set.add((x,y,a))
        
        if b == 0:
            if (x,y,a) in frame_set:
                frame_set.remove((x,y,a))
            else:
                continue
                
            if not check_is_okay():
                frame_set.add((x,y,a))
        
    answer = []
    for frame in frame_set:
        answer.append(list(frame))
    
    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    
    
    
    return answer