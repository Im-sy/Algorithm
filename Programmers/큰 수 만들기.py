from itertools import combinations


def solution(number, k):
    answer = []
    for num in number:
        while answer and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)

    ## 시간 초과
    # for comb in combinations(number, len(number)-k):
    #     if answer < ''.join(comb):
    #         answer = ''.join(comb)
    # return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
