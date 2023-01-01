T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    M = format(M, 'b')
    print(M)
    cnt = 0
    for i in range(len(M)-1, -1, -1):
        if M[i] == '0':
            ans = 'OFF'
            break
        else:
            cnt += 1
    if cnt >= N:
        ans = 'ON'
    print(f'#{tc} {ans}')