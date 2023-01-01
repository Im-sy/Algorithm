import sys
sys.stdin = open('swea_1961.txt', 'r')

def rotate(N, arr):
    tmp_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp_arr[i][j] = arr[N - 1 - j][i]
    return tmp_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr90 = rotate(N, arr)
    arr180 = rotate(N, arr90)
    arr270 = rotate(N, arr180)
    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, arr90[i])), end=' ')
        print(''.join(map(str, arr180[i])), end=' ')
        print(''.join(map(str, arr270[i])), end=' ')
        print()
