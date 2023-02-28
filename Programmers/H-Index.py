def solution(citations):
    citations.sort(reverse=True)
    # print(citations)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)


print(solution([3, 0, 6, 1, 5]))
print(solution([6, 5, 5, 5, 3, 2, 1, 0]))