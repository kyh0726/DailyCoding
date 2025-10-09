import heapq
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    answer = [[]]
    pre_order_result = []
    post_order_result = []
    node_heap = []
    new_tree = defaultdict(list)
    
    for idx, node in enumerate(nodeinfo):
        node_num = idx + 1
        x,y = node
        heapq.heappush(node_heap, (-y, x, node_num))
    
    def insert_node(target_node, new_node, x, y):
        node_link, pos = new_tree[target_node]
        
        left_link, right_link = node_link
        target_x, target_y = pos
        
        # x값이 더 작으면 left_link로
        if x < target_x:
            # 연결 되어있지 않은 경우에는 링크 갱신
            if left_link == -1:
                new_tree[new_node] = [(-1,-1), (x,y)]
                new_tree[target_node][0] = (new_node, right_link)
            # 연결된 경우에는 연결된 노드에서 같은 작업 수행
            else:
                insert_node(left_link, new_node, x, y)
        
        # 더 크면 right_link로
        else:
            if right_link == -1:
                new_tree[new_node] = [(-1,-1), (x,y)]
                new_tree[target_node][0] = (left_link, new_node)
            else:
                insert_node(right_link, new_node, x, y)
                
    def pre_order(root_node):
        if root_node == -1:
            return
        pre_order_result.append(root_node)
        pre_order(new_tree[root_node][0][0])
        pre_order(new_tree[root_node][0][1])
        return
    
    def post_order(root_node):
        if root_node == -1:
            return
        post_order(new_tree[root_node][0][0])
        post_order(new_tree[root_node][0][1])
        post_order_result.append(root_node)
        return

    y,x,node_num = heapq.heappop(node_heap)
    root_node = node_num
    pos = (x,-y)
    # 위치 정보와 다음 노드에 대한 정보가 들어있음.
    new_tree[root_node] = [(-1,-1), pos]

    
    
    while node_heap:
        y, x, node_num = heapq.heappop(node_heap)
        y *= -1
        insert_node(root_node, node_num, x, y)
    pre_order(root_node)
    post_order(root_node)
    answer = [pre_order_result, post_order_result]
    return answer