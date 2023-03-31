import heapq


def solution(n, works):
    answer = 0
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
    while n > 0:
        M = -heapq.heappop(hq)
        heapq.heappush(hq, -(M-1))
        n -= 1
    for x in hq:
        if x < 0:
            answer += x**2
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))