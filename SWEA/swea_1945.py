T = int(input())
for tc in range(1, T+1):
    num = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0]*5
    for i in range(5):
        while num%prime[i] == 0:
            num //= prime[i]
            cnt[i] += 1
    result = ' '.join(map(str, cnt))
    print(f'#{tc} {result}')