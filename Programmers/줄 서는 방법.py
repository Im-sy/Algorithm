from itertools import permutations
import math


def solution(n, k):
    answer = []
    numbers = [_ for _ in range(1, n+1)]
    while numbers:
        # print(numbers, k)
        num_len = len(numbers)-1
        if num_len == -1:
            num_len = 0
        fact = math.factorial(num_len)
        time = k // fact
        k = k - time * fact
        if k % fact == 0:
            time -= 1
        # print(time)
        answer.append(numbers[time])
        numbers.pop(time)
    return answer
    ## 효율성 시간 초과
    # answer = []
    # time = k // math.factorial(n-1) + 1
    # # print(time)
    # numbers = [time] + [i for i in range(1, n+1) if i != time]
    # i = (time - 1) * math.factorial(n-1) + 1
    # # print(i)
    # for perm in permutations(numbers):
    #     # print(perm)
    #     if i == k:
    #         return list(perm)
    #     i += 1
    # return answer
    ## 효율성 시간 초과
    # answer = []
    # numbers = [i for i in range(1, n+1)]
    # i = 1
    # for perm in permutations(numbers):
    #     # print(perm)
    #     if i == k:
    #         return list(perm)
    #     i += 1
    # return answer


print(solution(3, 5))