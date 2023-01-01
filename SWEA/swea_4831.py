T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt_list = [0]*(N+1)
    for i in arr:
        cnt_list[i] = 1
    idx = K
    cnt = 0
    while idx < N:
        for j in range(K):
            if cnt_list[idx-j]:
                cnt += 1
                idx += K-j
                break
        else:
            cnt = 0
            break
        # if cnt_list[idx]:
        #     cnt += 1
        # else:
        #     for j in range(1, K-1):
        #         if cnt_list[idx-j]:
        #             cnt += 1
        #             idx = j
        #             break
        #     else:
        #         cnt = 0
        #         break
        # idx += K
    print(f'#{tc} {cnt}')