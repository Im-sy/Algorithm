from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            for comb in combinations(order, c):
                menu.append(tuple(sorted(comb)))
        menu = dict(Counter(menu))
        # print(menu)
        if menu:
            top = max(menu.values())
            if top < 2:
                continue
            top_menu = [''.join(x) for x in menu.keys() if menu[x] == top]
            answer += top_menu

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))