import sys

# 입력을 한꺼번에 읽어와서 처리하면 훨씬 빠릅니다.
input_data = sys.stdin.read().split()
if not input_data:
    exit()

M = int(input_data[0])
N = int(input_data[1])

# 테두리 전체 성장량을 담을 1차원 배열 (ㄴ자를 펼친 모양)
# 크기: (M-1) + 1 + (M-1) = 2M-1
line = [0] * (2 * M - 1)

# N일 동안의 성장량을 누적
idx = 2
for _ in range(N):
    zeros = int(input_data[idx])
    ones = int(input_data[idx+1])
    twos = int(input_data[idx+2])
    idx += 3
    
    for i in range(zeros, zeros + ones):
        line[i] += 1
    for i in range(zeros + ones, 2 * M - 1):
        line[i] += 2

# 최종 출력용 board 구성
# 0행(맨 윗줄) 미리 계산
top_row = [line[i] + 1 for i in range(M - 1, 2 * M - 1)]

# 결과 출력
output = []
# 0행 추가
output.append(" ".join(map(str, top_row)))

# 1행부터 M-1행까지 출력
for i in range(1, M):
    # i행의 0열 값은 line[M-1-i] + 초기값 1
    # 나머지 1열~M-1열은 top_row[1:]를 그대로 복제
    row = [str(line[M - 1 - i] + 1)] + list(map(str, top_row[1:]))
    output.append(" ".join(row))

sys.stdout.write("\n".join(output) + "\n")