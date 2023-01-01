def solve(n, r, c):
    if n == 1:
        return arr[r][c]
    nn = n//3
    num1 = solve(nn, r, c)
    num2 = solve(nn, r, c+nn)
    num3 = solve(nn, r, c+nn*2)
    num4 = solve(nn, r+nn, c)
    num5 = solve(nn, r+nn, c+nn)
    num6 = solve(nn, r+nn, c+nn*2)
    num7 = solve(nn, r + nn*2, c)
    num8 = solve(nn, r + nn*2, c + nn)
    num9 = solve(nn, r + nn*2, c + nn * 2)
    if num1==num2==num3==num4==num5==num6==num7==num8==num9 and num1 in ['0','1','-1']:
        return num1
    return num1+num2+num3+num4+num5+num6+num7+num8+num9

import sys
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
ans = solve(N, 0, 0)
minus = ans.count('-1')
zero = ans.count('0')
print(minus)
print(zero)
print(len(ans)-2*minus-zero)