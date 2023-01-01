# 1206

# 파일에서 바로 읽어오기 제출할 땐 sys 부분 지우고 제출
import sys
sys.stdin = open('input.txt', 'r')

# 자신과 왼쪽 두 개, 오른쪽 두 개와의 높이 차를 사용
# 높이 차 중에서 가장 작은 값을 사용하고, 이 수는 양수여야 한다.

for tc in range(1, 11): # test case 10개
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2): # 시작 2개, 마지막 2개 제외한 범위
        min_h = 255 # 빌딩 높이는 최대 255, 가장 작은 값 찾기 위한 기준
        for j in range(-2, 3):
            if j != 0:
                h = arr[i] - arr[i + j] # i-2, i-1, i+1, i+2 와의 높이 차
                if min_h > h: # 높이 차 중에서 가장 작은 값 찾기 위한 부분
                    min_h = h
        if min_h > 0: # 음수라면 자신보다 높은 빌딩이 있다는 것
            cnt += min_h
    print(f'#{tc} {cnt}')