def solution(n):
    answer = 0
    third = []
    while n > 0:
        third.append(str(n%3))
        n //= 3
    reversed(third)
    # print(third)
    tmp = 1
    while third:
        answer += tmp*int(third.pop())
        tmp *= 3
    ## 3진수 -> 10진수로 바꾸는 법
    # answer = int(third, 3)
    return answer


print(solution(45))
print(solution(125))