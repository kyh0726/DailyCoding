import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
def solution(k, room_number):
    answer =[]
    N = len(room_number)
    room_info = defaultdict(int)
    def find(x):
        if not room_info[x]:
            room_info[x] = x
        if room_info[x] != x:
            room_info[x] = find(room_info[x])
        return room_info[x]
        
    def union(x,y):
        x = find(x)
        y = find(y)
        
        room_info[x] = y
        
    
        
    for number in room_number:
        root = find(number)
        answer.append(root)
        union(root, root + 1)
    return answer
