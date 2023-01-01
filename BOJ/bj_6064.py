# 1 1
# 2 2
# ...
# 9 9
# 10 10
# 1 11
# 2 12
# 3 1
# 4 2
# ...

def lcm(a, b):
    A, B = a, b
    while b:
        a, b = b, a%b
    if a == 0:
        return 0
    return (A*B)/a

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    last = lcm(M, N)
    while x<=last:
        if (x-y)%N == 0:
            print(x)
            break
        x += M
    else:
        print(-1)