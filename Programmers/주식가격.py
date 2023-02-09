from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        cnt = 0
        for p in prices:
            cnt += 1
            if p < price:
                break
        answer.append(cnt)
    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([5, 4, 3, 2, 5]))