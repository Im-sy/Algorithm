T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0]*1001
    for _ in range(N):
        bus_type, start, end = map(int, input().split())
        if bus_type == 1:
            for i in range(start, end+1):
                bus_stop[i] += 1
        elif bus_type == 2:
            for i in range(start, end, 2):
                bus_stop[i] += 1
            bus_stop[end] += 1
        else:
            if start%2:
                for i in range(start, end+1):
                    if i%3 == 0 and i%10 != 0:
                        bus_stop[i] += 1
            else:
                for i in range(start, end+1):
                    if i%4 == 0:
                        bus_stop[i] += 1
    tmp_max = 0
    for x in bus_stop:
        if tmp_max < x:
            tmp_max = x
    print(f'#{tc} {tmp_max}')