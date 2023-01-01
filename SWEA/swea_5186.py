T = int(input())

def f_to_bin(f):
    global ans
    while f != 1.0:
        f *= 2
        if f > 1:
            ans += '1'
            f -= 1
        elif f < 1:
            ans += '0'
        if len(ans) > 12:
            return 'overflow'
    return ans+'1'


for tc in range(1, T+1):
    num = float(input())
    ans = ''
    print(f'#{tc} {f_to_bin(num)}')