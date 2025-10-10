from collections import deque
import sys
sys.setrecursionlimit(10**5)

def solution(n, m, x, y, r, c, k):
    # 우선순위 아래 > 왼쪽 > 오른쪽 > 위
    moves = [(1,0),(0,-1),(0,1),(-1,0)]
    dirs = ["d", "l", "r", "u"]
    dist = abs(x-r) + abs(y-c)
    if dist % 2 != k % 2:
        return "impossible"
    if k < dist:
        return "impossible"
    
    def dfs(row,col,count,string):
        if count == k: 
            if (row,col) == (r,c):
                return string
        else:
            for i in range(4):
                dr, dc = moves[i]
                direction = dirs[i]
                next_r, next_c = row + dr, col + dc    
                if 0 < next_r <= n and 0 < next_c <= m:
                    if abs(next_r - r) + abs(next_c - c) + count + 1 > k:
                        continue    
                    res = dfs(next_r,next_c,count+1,string+direction)
                    if res is not None:
                        return res
    answer = dfs(x,y,0,"")
                
    
    if answer is None:
        return "impossible"
    else:
        return answer
    