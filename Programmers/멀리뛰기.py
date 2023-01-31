import math


def solution(n):
    answer = 0
    two = n//2
    while two >= 0:
        answer += math.factorial(two + (n-2*two)) // (math.factorial(two) * math.factorial(n-2*two))
        two -= 1
    return answer % 1234567


print(solution(4))
print(solution(3))
print(solution(2000))