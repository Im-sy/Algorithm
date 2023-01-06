def solution(numbers, target):
    answer = 0

    def dfs(idx, sign, tmp):
        nonlocal answer
        if idx == len(numbers):
            if tmp == target:
                answer += 1
            return
        tmp += numbers[idx] * sign
        dfs(idx + 1, 1, tmp)
        dfs(idx + 1, -1, tmp)

    dfs(0, 1, 0)
    dfs(0, -1, 0)

    return answer//2


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))