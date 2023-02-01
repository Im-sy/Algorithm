import re
from collections import Counter


def preprocess(string):
    string = [''.join(string[i:i + 2]).lower() for i in range(len(string) - 1)]
    for x in string.copy():
        if re.findall(r'[^a-zA-Z]', x):
            string.remove(x)
    return string


def solution(str1, str2):
    str1 = preprocess(str1)
    str2 = preprocess(str2)
    # print(str1, str2)

    u = 0
    n = 0
    union = dict(Counter(str1 + str2))
    str1 = dict(Counter(str1))
    str2 = dict(Counter(str2))
    for k, v in union.items():
        if str1.get(k) is None:
            str1[k] = 0
        if str2.get(k) is None:
            str2[k] = 0
        if v > 1:
            n += min(str1[k], str2[k])
        u += max(str1[k], str2[k])
    # print(union)
    # print(u, n)

    if u == 0:
        answer = 1
    else:
        answer = n/u
    return int(answer*65536)


# set 사용한 다른 사람의 풀이 참고
def solution2(str1, str2):
    str1 = preprocess(str1)
    str2 = preprocess(str2)

    n = set(str1) & set(str2)
    u = set(str1) | set(str2)
    if len(u) == 0:
        answer = 1
    else:
        n_sum = sum([min(str1.count(x), str2.count(x)) for x in n])
        u_sum = sum([max(str1.count(x), str2.count(x)) for x in u])
        answer = n_sum/u_sum
    return int(answer*65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))