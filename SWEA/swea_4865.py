T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    max_cnt = 0
    for x in str1:
        cnt = 0
        for j in range(M):
            if x == str2[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')