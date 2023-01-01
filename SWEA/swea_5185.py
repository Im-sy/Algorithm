T = int(input())

def hex_to_dec(h):
    if h in '0123456789':
        return int(h)
    else:
        return ord(h)-ord('A')+10

def dec_to_bin(d):
    bits = ['0']*4
    idx = 3
    while d>0:
        bits[idx] = str(d%2)
        d //= 2
        idx -= 1
    return ''.join(bits)

for tc in range(1, T+1):
    N, arr = input().split()
    ans = ''
    for i in range(int(N)):
        ans += dec_to_bin(hex_to_dec(arr[i]))
    print(f'#{tc} {ans}')