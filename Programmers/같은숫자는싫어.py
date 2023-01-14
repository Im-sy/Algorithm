from collections import deque


def solution(arr):
    answer = []
    arr = deque(arr)
    while arr:
        first = arr.popleft()
        if not answer:
            answer.append(first)
        elif answer[-1] != first:
            answer.append(first)
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))