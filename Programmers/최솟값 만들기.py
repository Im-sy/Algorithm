def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    # print(A, B)
    while A:
        answer += A.pop() * B.pop()

    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))