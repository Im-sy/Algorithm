import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))
cnt = abs(100-N)
# 0 100
# 1 100
# 50 100
# 56, 57, 58 X
# 5455 6
# 5459 6
# N에 가까운 수(절댓값) 찾기 위해서 n 늘려가기
# n 안에 고장난 숫자 있으면 break
# 없으면 가까운 수 중에 제일 작은지 확인
# 현재 수와 N과의 차이에 n길이만큼 더한게 움직인 횟수

for n in range(1000001):
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) in broken:
            break
        elif i == len(n)-1:
            # 현재 -> N으로 가기 위한 클릭 횟수
            cnt = min(cnt, abs(int(n)-N)+len(n))
print(cnt)