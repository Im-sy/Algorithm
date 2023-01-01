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

num = {'001101': '0',
        '010011': '1',
        '111011': '2',
        '110001': '3',
        '100011': '4',
        '110111': '5',
        '001011': '6',
        '111101': '7',
        '011001': '8',
        '101111': '9'}

password = get_bin('0269FAC9A0')
for i in range(len(password)-1, -1, -1):
    if password[i]=='1':
        idx = i
        break
result = []
while idx>=6:
    result.append(num[password[idx-5:idx+1]])
    idx -= 6
for x in range(len(result)-1, -1, -1):
    print(result[x], end=' ')
