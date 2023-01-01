T = int(input())
# 회문인지 판단하는 함수
def rev(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True

# NxN 배열에서 길이 M인 회문 찾는 함수
def find():
    for i in range(N):
        # 가로(행)방향
        for j in range(N-M+1):
            tmp = arr[i][j:j+M]
            if rev(tmp):
                return tmp
        # 세로(열)방향
        for j in range(N-M+1):
            tmp = ''
            for k in range(M):
                tmp += arr[j+k][i]
            if rev(tmp):
                return tmp

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {find()}')