import sys
import math
from collections import defaultdict, deque

N = int(sys.stdin.readline().strip())

requires = defaultdict()
needs = defaultdict()
moves = [(1,0),(-1,0), (0,1),(0,-1)]

# 대문자 A 아스키 코드 65
# 소문자 a 아스키 코드 97    
  

for _ in range(N):
  def bfs(keys, R, C):
    q = deque()
    result = 0
    q.append((0,0))
    visited[0][0] = True
    # waiting_set에 필요한 열쇠가 키값, 그리고 해금되는 좌표 쪽이 리스트로 저장됨
    waiting_set = defaultdict(list)
    # 내가 갖고 있는 키
    my_keys = set()
    for key in keys:
      my_keys.add(key)

    while q:
      row, col = q.popleft()

      for dr, dc in moves:
        next_r, next_c = row + dr, col + dc
        
        if next_r >= (R+2) or next_c >= (C+2) or next_r < 0 or next_c < 0:
          continue
        if visited[next_r][next_c]:
          continue
        
        if board[next_r][next_c] == ".":
          visited[next_r][next_c] = True
          q.append((next_r, next_c))
          continue
        
        # 다음 방문하는 곳이 문일 때
        if ord("A") <= ord(board[next_r][next_c]) <= ord("Z"):
          key = chr(ord(board[next_r][next_c]) + 32)
          if key in my_keys:
            q.append((next_r,next_c))
            visited[next_r][next_c] = True
            continue
          else:
            waiting_set[key].append((next_r, next_c))
            continue
            
        # 다음 방문하는 곳이 키일 때
        if ord("a") <= ord(board[next_r][next_c]) <= ord("z"):
          key = board[next_r][next_c]
          # 키에 추가하고 큐에도 넣기
          my_keys.add(key)
          q.append((next_r,next_c))
          visited[next_r][next_c] = True
          # 기다리는 좌표가 있으면
          while waiting_set[key]:
            r,c = waiting_set[key].pop()
            q.append((r,c))
            visited[r][c] = True
          
          continue

        if board[next_r][next_c] == "$":
          result += 1
          visited[next_r][next_c] = True
          q.append((next_r, next_c))

    return result
      


      


  R, C = map(int, sys.stdin.readline().strip().split())
  visited = [[False] * (C+2) for _ in range(R+2)]

  board = []
  board.append(["."]* (C+2))
  for __ in range(R):
    board.append(["."] +list(sys.stdin.readline().strip()) + ["."])
  board.append(["."]* (C+2))

  

  keys = list(sys.stdin.readline().strip())

  answer = bfs(keys, R, C)
  print(answer)