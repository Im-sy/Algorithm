def solution(n, m, section):
    answer = 0
    idx = 0
    for s in section:
        if idx < s:
            answer += 1
            idx = s + m - 1
    return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))