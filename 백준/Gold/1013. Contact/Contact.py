import sys
import re

# 테스트 케이스 개수 입력
t = int(sys.stdin.readline())

# 정규표현식 패턴 정의
# ^와 $를 써서 문자열의 시작과 끝이 정확히 일치하도록 함
pattern = re.compile(r'(100+1+|01)+')

for _ in range(t):
    signal = sys.stdin.readline().strip()
    
    # 패턴과 완벽히 일치하는지 확인
    if pattern.fullmatch(signal):
        print("YES")
    else:
        print("NO")