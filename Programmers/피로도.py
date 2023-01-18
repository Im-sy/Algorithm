from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for perm in permutations(dungeons):
        now = k
        tmp = 0
        for [a, b] in perm:
            if now >= a and now-b >= 0:
                now -= b
                tmp += 1
        answer = max(answer, tmp)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))