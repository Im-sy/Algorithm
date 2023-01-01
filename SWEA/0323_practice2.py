# 16진수 -> 10진수
def hex_to_dec(h):
    if h in '0123456789':
        return ord(h) - ord('0')
    else:
        return ord(h) - ord('A') + 10

# 10진수 -> 4비트 2진수
def dec_to_bin(d):
    bits = ['0']*4
    idx = 3
    while d > 0:
        bits[idx] = str(d % 2)
        d //= 2
        idx -= 1
    return ''.join(bits)

def get_bin(data):
    binary = ''
    for d in data:
        binary += dec_to_bin(hex_to_dec(d))
    return binary

print(get_bin('01D06079861D79F99F'))
