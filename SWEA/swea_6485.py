T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [0]*5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus[i] += 1
    P = int(input())
    bus_c = []
    for i in [int(input()) for _ in range(P)]:
        # print(bus[i], end=' ')
        bus_c.append(bus[i])
    result = ' '.join(map(str, bus_c))
    print(f'#{tc} {result}')