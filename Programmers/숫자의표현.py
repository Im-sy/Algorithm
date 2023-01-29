def solution(n):
    answer = 0
    tmp_n = n
    for i in range(1, n//2+2):
        tmp_n -= i
        if tmp_n < 0:
            break
        if tmp_n % i == 0:
            answer += 1

    return answer


print(solution(15))
print(solution(3))