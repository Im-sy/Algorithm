from itertools import combinations


def solution(brown, yellow):
    whole = brown + yellow
    divisor = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisor.append(i)
    if len(divisor) % 2 == 1:
        divisor.append(divisor[len(divisor)//2])
    for a, b in combinations(divisor, 2):
        if (a+2)*(b+2) == whole:
            return [b+2, a+2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))