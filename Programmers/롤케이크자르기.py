from collections import Counter


def solution(topping):
    answer = 0
    right = dict(Counter(topping))
    left = set()
    while topping:
        t = topping.pop()
        left.add(t)
        if right[t] > 1:
            right[t] -= 1
        else:
            del right[t]
        print(left, right)
        if len(left) == len(right):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))