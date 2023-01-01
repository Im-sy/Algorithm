T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201
    for _ in range(N):
        now, back = map(int, input().split())
        now = (now+1)//2
        back = (back+1)//2
        if now < back:
            for i in range(now, back+1):
                corridor[i] += 1
        else:
            for i in range(back, now+1):
                corridor[i] += 1
    tmp_max = 0
    for i in range(201):
        if tmp_max < corridor[i]:
            tmp_max = corridor[i]
    print(f'#{tc} {tmp_max}')