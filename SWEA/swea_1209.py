import sys
sys.stdin = open('swea_1209.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_tmp_rc_1 = sum_tmp_rc_2 = max_tmp = 0
    for i in range(100):
        sum_tmp_r = sum_tmp_c = 0
        for j in range(100):
            sum_tmp_r += arr[i][j]
            sum_tmp_c += arr[j][i]
        if sum_tmp_r > max_tmp:
            max_tmp = sum_tmp_r
        if sum_tmp_c > max_tmp:
            max_tmp = sum_tmp_c

        sum_tmp_rc_1 += arr[i][i]
        sum_tmp_rc_2 += arr[i][99-i]

        if sum_tmp_rc_1 > max_tmp:
            max_tmp = sum_tmp_rc_1
        if sum_tmp_rc_2 > max_tmp:
            max_tmp = sum_tmp_rc_2
    print(f'#{tc} {max_tmp}')