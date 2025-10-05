
            
        
        
def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    cursor = k
    deleted_list = []
    answer= ''
    def move(cursor, val):
        if val < 0:
            temp = cursor
            for i in range(-val):
                temp = linked_list[temp][0]
            return temp
        else:
            temp = cursor
            for i in range(val):
                temp = linked_list[temp][1]
            return temp
    
    def delete_node(idx):
        prev_node = linked_list[idx][0]
        next_node = linked_list[idx][1]
        deleted_list.append((idx, prev_node, next_node))
        # 삭제된 노드는 -2,-2로 플래그 남기기
        linked_list[idx] = [-2,-2]

        # 이전 노드가 없는 경우는 그 다음 노드만 바꿔주기
        if prev_node == -1:
            linked_list[next_node][0] = -1
            return next_node
        
        # 다음 노드가 없는 경우는 이전 노드만 이어주기
        if next_node == n:
            linked_list[prev_node][1] = n
            return prev_node
        
        # 이외의 경우는 이전, 이후 노드 이어주기  & 바로 아래행 선택해서 리턴
        linked_list[prev_node][1] = next_node
        linked_list[next_node][0] = prev_node
        return next_node
    
    def insert_node():
        val, prev_node, next_node = deleted_list.pop()
        
        # prev_node 가 없었던 경우
        if prev_node == -1 or linked_list[prev_node] == [-2,-2]:
            linked_list[val][1] = next_node
            linked_list[val][0] = -1
            linked_list[next_node][0] = val
            return
        
        # next_node 가 없었던 경우
        if next_node == n or linked_list[next_node] == [-2,-2]:
            linked_list[val][1] = n
            linked_list[val][0] = prev_node
            linked_list[prev_node][1] = val
            return
        
        linked_list[val][1] = next_node
        linked_list[val][0] = prev_node
        linked_list[prev_node][1] = val
        linked_list[next_node][0] = val
        return
            
                
        
        
        
        
    
    for command in cmd:

        if command[0] == "D":
            action, val = command.split()
            cursor = move(cursor, int(val))
        if command[0] == "U":
            action, val = command.split()
            cursor = move(cursor, -int(val))
        if command[0] == "C":
            cursor = delete_node(cursor)
        if command[0] == "Z":
            insert_node()
    
    for i in range(n):
        if linked_list[i] == [-2,-2]:
            answer += "X"
        else:
            answer += "O"
    
    return answer