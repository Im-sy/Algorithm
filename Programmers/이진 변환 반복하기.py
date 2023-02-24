def make_bin(l):
    res = ''
    while l>0:
        res = str(l%2) + res
        l //= 2
    return res


def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        zero += s.count('0')
        one = s.count('1')
        s = make_bin(one)
        # print(s)
        cnt += 1
    return [cnt, zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))