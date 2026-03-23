import sys


    



while True:

    N = int(sys.stdin.readline().strip())

    if N == 0:
        exit(0)

    
    rooms = [0] + [list(sys.stdin.readline().strip().split()) for _ in range(N)]
    visited = [False] * (N+1)
    def dfs(cur_money, cur_room_idx, target_room):
        cur_room = rooms[cur_room_idx]
                
        if cur_room[0] == "T":
            cur_money -= int(cur_room[1])
        
        if cur_room[0] == "L":
            cur_money = max(int(cur_room[1]), cur_money)


        if cur_money < 0:
            return False

        if cur_room_idx == target_room:
            return True


        for next_room_idx in map(int, cur_room[2:-1]):
            if visited[next_room_idx]:
                continue
            else:
                visited[next_room_idx] = True
                result = dfs(cur_money, next_room_idx, target_room)
                visited[next_room_idx] = False
                if result:
                    return True
        
        return False

    
    
    result = dfs(0, 1, N)

    if result:
        print("Yes")
    else:
        print("No")
