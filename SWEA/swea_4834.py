T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt_list = [0]*10
    for i in range(N):
        cnt_list[arr[i]] += 1
    max_num = 0
    max_cnt = 0
    for i in range(10):
        if max_cnt <= cnt_list[i]:
            max_num = i
            max_cnt = cnt_list[i]
    print(f'#{tc} {max_num} {max_cnt}')