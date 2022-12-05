from itertools import combinations_with_replacement
from collections import Counter


def get_score(ryan, apeach):
    score = 0
    for i in range(11):
        if ryan.get(i, 0) == apeach.get(i, 0) == 0:
            continue
        if ryan.get(i, 0) > apeach.get(i, 0):
            score += i
        else:
            score -= i
    return score


def get_priority(ryan, apeach):
    for i in range(11):
        if ryan.get(i, 0) > apeach.get(i, 0):
            return ryan
        elif ryan.get(i, 0) < apeach.get(i, 0):
            return apeach


def solution(n, info):
    max_score = -float('INF')
    max_score_dict = None
    info_counter = dict([(10-i, cnt) for (i, cnt) in enumerate(info) if cnt > 0])
    for comb in combinations_with_replacement(range(11), n):
        comb_counter = Counter(comb)
        tmp_score = get_score(comb_counter, info_counter)
        if max_score < tmp_score:
            max_score = tmp_score
            max_score_dict = comb_counter
        elif max_score == tmp_score:
            max_score_dict = get_priority(comb_counter, max_score_dict)

    if max_score <= 0:
        return [-1]

    answer = [0]*11
    for k, v in max_score_dict.items():
        answer[10-k] = v

    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))