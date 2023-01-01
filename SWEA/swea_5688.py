T = int(input())
import math
for tc in range(1, T+1):
    N = int(input())
    x = N**(1/3)
    if math.isclose(round(x), x):
        print(f'#{tc} {round(x)}')
    else:
        print(f'#{tc} -1')