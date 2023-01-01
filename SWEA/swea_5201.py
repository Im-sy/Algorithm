T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    result = []
    ans = 0
    while len(result)<=M:
        if not container or not truck:
            ans = sum(result)
            break
        ct, tt = container[0], truck[0]
        if ct <= tt:
            result.append(ct)
            container.pop(0)
            truck.pop(0)
        else:
            container.pop(0)
    else:
        ans = sum(result)
    print(f'#{tc} {ans}')