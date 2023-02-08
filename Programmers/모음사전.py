def solution(word):
    answer = 0
    alphabets = ["", "A", "E", "I", "O", "U"]
    result = []

    def dfs(n, words):
        if n == 0:
            result.append(words)
            return
        for i in range(6):
            dfs(n-1, words+alphabets[i])

    dfs(5, "")
    result = sorted(list(set(result)))
    # print(result)
    answer = result.index(word)
    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))