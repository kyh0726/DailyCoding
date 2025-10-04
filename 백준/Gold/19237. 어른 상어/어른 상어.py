import sys
import heapq

# 냄새가 아예 없는 곳
# 내 냄새가 있는 곳
# 다른 상어 냄새가 있는 곳

# 겹치면 number가 높은 상어가 튕겨져 나간다
# board[N][N][0]는 상어의 위치
# board[N][N][1]는 상어의 냄새 여부

N, M, K = map(int, sys.stdin.readline().strip().split())
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
board = [list(map(lambda x: [[-int(x)],[]], sys.stdin.readline().strip().split())) for _ in range(N)]
priorities = [[] for _ in range (M+1)]
priorities[0].append([])
shark_dirs = [0] + list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))

for i in range(1,M+1):
  for j in range(4):
    priorities[i].append(list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())))





for T in range(1,1001):
  shark_num = 0

  sharks_waiting_queue = []

  for num in range(1,M+1):
    r,c, = -1,-1
    for i in range(N):
      for j in range(N):
        if board[i][j][0] and num == -board[i][j][0][0]:
          r,c = i,j
          board[i][j][1].append((num, K))
    
    if (r,c) == (-1,-1):
      continue

    priority = priorities[num][shark_dirs[num]]
    dirty_priority_queue = []
    clean_priority_queue = []

    for dir,(dr,dc) in enumerate(dirs):
      next_r, next_c = r + dr, c + dc
      if next_r >= N or next_c >= N or next_r < 0 or next_c < 0:
        continue
      if board[next_r][next_c][1]:
        isMe = 0
        for target_num, time in board[next_r][next_c][1]:
          if target_num == num:
            isMe = -1
        # 내 냄새가 최 우선순위, 이후는 방향 우선순위대로..
        heapq.heappush(dirty_priority_queue, (isMe , priority.index(dir), dir))
      if not board[next_r][next_c][1]:
        heapq.heappush(clean_priority_queue, (priority.index(dir), dir))

    isPopped = False
    next_dir = 0
    # 냄새 안나는 곳만 남은 경우
    while clean_priority_queue and not isPopped:
      next_dir = heapq.heappop(clean_priority_queue)[1]
      isPopped = True
      break
    
    # 냄새 나는 곳만 남은 경우
    while dirty_priority_queue and not isPopped:
      next_dir = heapq.heappop(dirty_priority_queue)[2]
      isPopped = True
      break
    
    # 방향 바꾸고 대기 큐에 넣었다가 마지막에 한 꺼번에 바꿀 계획
    shark_dirs[num] = next_dir
    sharks_waiting_queue.append((num, r + dirs[next_dir][0], c + dirs[next_dir][1]))
  
  # 물고기 이전 위치 다 지워
  for i in range(N):
    for j in range(N):
      board[i][j][0] = []

  for shark in sharks_waiting_queue:
    num, row, col = shark
    # 음수로 넣어서 가장 큰 숫자 먼저 튕기게 하기
    heapq.heappush(board[row][col][0], -num)  
    while board[row][col][0] and len(board[row][col][0]) > 1:
      heapq.heappop(board[row][col][0])

  # 냄새 시간 초기화해주기
  for i in range(N):
    for j in range(N):
      if board[i][j][0]:
        shark_num += 1
      smell_waiting_queue = []
      while board[i][j][1]:
        num, time = board[i][j][1].pop()
        if time - 1 == 0:
          continue
        smell_waiting_queue.append((num, time))

      for num, time in smell_waiting_queue:
        board[i][j][1].append((num, time-1))

  if shark_num == 1:
    print(T)
    exit(0)








print(-1)