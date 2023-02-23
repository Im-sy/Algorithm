from collections import deque
import copy


def solution(elements):
    answer = set()
    elements = deque(elements)
    copy_elements = copy.deepcopy(elements)
    n = len(elements)
    while True:
        for i in range(n):
            answer.add(sum(list(elements)[:i+1]))
        elements.rotate(-1)
        if elements == copy_elements:
            break
    return len(answer)
    ## 시간 초과
    # answer = set()
    # n = len(elements)
    # for i in range(n):
    #     for l in range(1, n+1):
    #         tmp = []
    #         for idx in range(i, i+l):
    #             if idx >= n:
    #                 idx -= n
    #             tmp.append(elements[idx])
    #         answer.add(sum(tmp))
    # return len(answer)

    ## 다른 풀이.. 시간 많이 줄일 수 있음!!!!
    # answer = set()
    # n = len(elements)
    # for i in range(n):
    #     tmp = elements[i]
    #     answer.add(tmp)
    #     for j in range(i+1, i+n):
    #         tmp += elements[j%n]
    #         answer.add(tmp)
    # return len(answer)



print(solution([7, 9, 1, 1, 4]))