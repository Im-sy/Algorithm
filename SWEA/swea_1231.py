def in_order(v):
    if v:
        in_order(ch1[v])
        print(node[v-1][1], end='')
        in_order(ch2[v])

for tc in range(1, 11):
    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    node = [list(input().split()) for _ in range(N)]
    for i in range(N):
        if len(node[i])>2:
            ch1[i+1] = int(node[i][2])
            try:
                ch2[i+1] = int(node[i][3])
            except IndexError:
                pass
    print(ch1, ch2)
    print(f'#{tc}', end=' ')
    in_order(1)