import sys
from collections import defaultdict
moves = [(1,-1), (1,0), (1,1), (0,-1), (0,0), (0,1), (-1,-1), (-1,0), (-1,1)]

R, C = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(R)]
result_board = [['.'] * C for _ in range(R)]
cmds = sys.stdin.readline().strip()

main_r, main_c = 0,0
robots = []

for i in range(R):
    for j in range(C):
        if board[i][j] == "R":
            robots.append((i,j))
        if board[i][j] == "I":
            main_r, main_c = i, j

def find_nearest_route(start, end):
    start_r, start_c = start
    end_r, end_c = end

    min_dist = 1e10
    min_pos = [start_r, start_c]


    # 가장 가까워지는 거리 탐색
    for dr, dc in moves:
        next_r, next_c = start_r + dr, start_c + dc
        dist = abs(next_r - end_r) + abs(next_c - end_c)

        if dist < min_dist:
            min_dist = dist
            min_pos = [next_r, next_c]

    return min_pos


for idx,cmd in enumerate(cmds):
    main_r, main_c = main_r + moves[int(cmd)-1][0], main_c + moves[int(cmd)-1][1]
    robot_visited = defaultdict(int)
    temp = []
    while robots:

        robot = robots.pop()
        next_robot_r, next_robot_c = find_nearest_route(robot, [main_r, main_c])

        if (next_robot_r, next_robot_c) == (main_r, main_c):
            print("kraj " + str(idx+1))
            exit(0)

        robot_visited[(next_robot_r,next_robot_c)] += 1
        temp.append((next_robot_r, next_robot_c))

    while temp:
        robot_r, robot_c = temp.pop()
        if robot_visited[(robot_r,robot_c)] > 1:
            continue
        robots.append((robot_r, robot_c))





result_board[main_r][main_c] = "I"
for robot_r, robot_c in robots:
    result_board[robot_r][robot_c] = "R"

for row in result_board:
    for val in row:
        print(val, end="")
    print()