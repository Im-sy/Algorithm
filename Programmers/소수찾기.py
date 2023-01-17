from itertools import permutations


def isprime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        for perm in set(permutations(list(map(str, numbers)), i)):
            num = int(''.join(perm))
            if isprime(num):
                answer.add(num)
    return len(answer)


print(solution("17"))
print(solution("011"))
