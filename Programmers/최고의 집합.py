def solution(n, s):
    answer = [s//n]*n
    if s%n:
        for i in range(1, s%n+1):
            answer[i] += 1
    if 0 in answer:
        answer = [-1]
    answer.sort()
    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
print(solution(3, 10))