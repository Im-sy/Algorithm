import math


def lcm(a, b):
    tmp = a * b
    while True:
        c = a % b
        if c == 0:
            gcd = b
            break
        a, b = b, c
    # print('gcd:', gcd)
    return tmp // gcd


def solution(arr):
    # answer = 1
    # for i in arr:
    #     answer = math.lcm(answer, i)
    answer = 1
    for a in arr:
        answer = lcm(answer, a)
    return answer


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([3, 4, 9, 16]))