import sys, copy
from collections import deque
from itertools import combinations
import heapq
N, M = map(int, sys.stdin.readline().strip().split())
seg_trees = [0] * 4 * N
arr = [0]
def make_seg_tree(idx, left, right):
    if left == right:
        seg_trees[idx] = arr[left]
        return seg_trees[idx]


    middle = (left + right) // 2
    seg_trees[idx] = min(make_seg_tree(idx*2, left, middle), make_seg_tree(idx*2 + 1, middle + 1, right))
    return seg_trees[idx]

def search_seg_trees(idx, left, right, start, end):

    if end < left or start > right:
        return 1e10
    if left <= start and end <= right:
        return seg_trees[idx]
    mid = ( start + end ) // 2
    return min(search_seg_trees(idx*2, left, right, start, mid), search_seg_trees(idx*2+1, left, right, mid+1, end))
    


for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))
make_seg_tree(1, 1, N)

for j in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(search_seg_trees(1, a, b, 1, N))
