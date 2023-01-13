from collections import deque


def solution(priorities, location):
    answer = 0
    indexes = deque([i for i in range(len(priorities))])
    while indexes:
        idx = indexes.popleft()
        priority = priorities[idx]
        for index in indexes:
            if priority < priorities[index]:
                indexes.append(idx)
                break
        else:
            answer += 1
            if idx == location:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))