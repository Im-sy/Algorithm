from itertools import combinations
from collections import Counter

# def solution(k, tangerine):
#     answer = k
#     for comb in combinations(tangerine, k):
#         # print(comb)
#         answer = min(answer, len(set(comb)))
#     return answer


def solution(k, tangerine):
    answer = 0
    cnt = sorted(Counter(tangerine).values(), reverse=True)
    for c in cnt:
        # if c < k:
        #     k -= c
        #     answer += 1
        # else:
        #     answer += 1
        #     break
        k -= c
        answer += 1
        if k <= 0:
            break
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))