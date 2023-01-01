# 시간 초과
def fibonacci(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    zero = 0
    one = 0
    # fibonacci(N)
    if N == 0:
        zero += 1
    elif N == 1:
        one += 1
    else:
        zero = one = 1
        for _ in range(N-2):
            zero, one = one, zero+one
    print(zero, one)