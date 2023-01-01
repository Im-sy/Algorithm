T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(enumerate(list(map(int, input().split())), 1))
    oven = []
    for _ in range(N):
        oven.append(pizza.pop(0))
    while len(oven)>1:
        if len(oven)<N and pizza:
            oven.append(pizza.pop(0))
        idx, cheese = oven.pop(0)
        if cheese//2:
            oven.append((idx, cheese//2))
    print(f'#{tc} {oven.pop(0)[0]}')