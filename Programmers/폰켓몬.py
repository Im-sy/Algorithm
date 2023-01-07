from collections import Counter


def solution(nums):
    answer = 0
    cnt = Counter(nums)
    target = len(nums)//2
    tmp = 0
    for mon in cnt.keys():
        if tmp == target:
            break
        answer += 1
        tmp += 1
    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))