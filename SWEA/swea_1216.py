import sys
sys.stdin = open('swea_1216.txt', 'r')

def rev(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True

def find():
    for M in range(100, 0, -1):
        for i in range(100):
            # 가로(행)방향
            for j in range(100-M+1):
                tmp = arr[i][j:j+M]
                if rev(tmp):
                    return M
            # 세로(열)방향
            for j in range(100-M+1):
                tmp = ''
                for k in range(M):
                    tmp += arr[j+k][i]
                if rev(tmp):
                    return M

for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]
    print(f'#{tc} {find()}')