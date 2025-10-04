import sys



def init(start, end, index):
   # 가장 끝에 도달 -> arr 삽입

   if start == end:
      tree[index] = arr[start]
      return tree[index]
   
   mid = ( start + end ) // 2

   # 초기에 값을 재귀적으로 채워나감
   tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
   return tree[index]

def interval_sum(start, end, index, left, right):
   if left > end or right < start:
      return 0
   if left <= start and end <= right:
      return tree[index]
   
   mid = ( start + end ) // 2

   # start 와 end가 변하면서 구간합인 부분을 더해준다.
   return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update_tree(start, end, index, target_idx, target_val):
   if target_idx < start or target_idx > end:
      return

   tree[index] += target_val

   if start == end:
      return
   mid = ( start + end ) // 2
   update_tree(start, mid, index * 2, target_idx, target_val)
   update_tree(mid + 1, end, index * 2 + 1, target_idx, target_val)

N, M, K = map(int, sys.stdin.readline().strip().split())
arr = []
tree = [0] * 4 * N
for i in range(N):
   arr.append(int(sys.stdin.readline().strip()))
init(0, N-1, 1)
for i in range(M+K):
   a,b,c = map(int, sys.stdin.readline().strip().split())
   if a == 1:
      update_tree(0, N-1, 1, b - 1, c - arr[b-1])
      arr[b-1] = c
   else:
      print(interval_sum(0, N-1, 1, b-1, c-1))
       







def init_tree(start, end, idx):
   
   if start == end:
      tree[idx] = arr[start]
      return tree[idx]

   mid = ( start + end ) // 2

   tree[idx] = init(start, mid, idx * 2) +init (mid + 1, end, idx * 2 + 1)
   return tree[idx]
   

def cal_sum(start, end, idx, left, right):
   if left > end or right < start:
      return 0 
