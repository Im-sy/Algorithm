from itertools import combinations


def solution(clothes):
    answer = 1
    cnt = dict()
    for name, what in clothes:
        if what in cnt.keys():
            cnt[what] += 1
        else:
            cnt[what] = 1
    # print(cnt)
    for num in cnt.values():
        answer *= (1+num)

    ## 1번 시간 초과
    # for i in range(1, len(set(cnt.keys()))+1):
    #     for comb in combinations(set(cnt.keys()), i):
    #         tmp = 1
    #         for c in comb:
    #             if len(comb) == 1:
    #                 answer += cnt[c]
    #                 tmp = 0
    #             else:
    #                 tmp *= cnt[c]
    #         answer += tmp
    #         # print(list(comb))
    return answer-1

# a b b c c
# a b c
# a b, b c, c a
# a, b, c
# (x+a)(x+b)(x+c)
# x^3 + (a+b+c)x^2 + (ab+bc+ca)x + abc
# (1+1)(1+2)(1+2) - 1
# (안 입는 경우+개수) 곱해서 모두 안 입는 경우 -1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]))