T = int(input())

# def hex_to_dec(h):
#     if h in '0123456789':
#         return int(h)
#     else:
#         return ord(h)-ord('A')+10
#
# def dec_to_bin(d):
#     bits = ['0']*4
#     idx = 3
#     while d > 0:
#         bits[idx] = str(d%2)
#         d //= 2
#         idx -= 1
#     return ''.join(bits)

def check(lst):
    tmp_sum = 0
    for i in range(8):
        if i % 2:
            tmp_sum += lst[i]
        else:
            tmp_sum += lst[i]*3

    if tmp_sum % 10:
        return False
    else:
        return True

num = {'211':0,
       '221':1,
       '122':2,
       '411':3,
       '132':4,
       '231':5,
       '114':6,
       '312':7,
       '213':8,
       '112':9}

hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]
    # binary = []
    # for x in arr:
    #     tmp = ''
    #     for i in x:
    #         tmp += dec_to_bin(hex_to_dec(i))
    #     if tmp not in binary:
    #         binary.append(tmp)
    # binary = []
    # for x in arr:
    #     tmp = ''
    #     for i in x:
    #         b = format(int(i, 16), 'b')
    #         while len(b) != 4:
    #             b = '0' + b
    #         tmp += b
    #     if tmp not in binary:
    #         binary.append(tmp)

    binary = []
    for x in arr:
        tmp = ''
        for i in x:
            tmp += hex_to_bin[i]
        if tmp not in binary:
            binary.append(tmp)

    result = []
    v = []
    ans = 0
    for i in range(len(binary)):
        n1 = n2 = n3 = 0
        if '1' not in binary[i]:
            continue
        for j in range(len(binary[i])-1, -1, -1):
            if n2 == 0 and n3 == 0 and binary[i][j]=='1':
                n1 += 1
            elif n1 and n3 == 0 and binary[i][j]=='0':
                n2 += 1
            elif n1 and n2 and binary[i][j]=='1':
                n3 += 1
            elif n3 and binary[i][j]=='0':
                tmp = min(n1, n2, n3)
                result.append(num[str(n3//tmp)+str(n2//tmp)+str(n1//tmp)])
                n1 = n2 = n3 = 0
                if len(result) == 8:
                    result = result[::-1]
                    if check(result) and (result not in v):
                        ans += sum(result)
                        v.append(result)
                    result = []
    print(binary)
    print(f'#{tc} {ans}')