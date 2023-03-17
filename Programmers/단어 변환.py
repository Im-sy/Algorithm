from collections import deque


def solution(begin, target, words):
    answer = float('INF')
    if target not in words:
        return 0
    q = deque([(begin, 0)])
    n = len(begin)
    k = len(words)
    v = [0]*k
    while q:
        w, cnt = q.popleft()
        if w == target:
            answer = min(answer, cnt)
        for i in range(k):
            tmp = 0
            for j in range(n):
                if w[j] != words[i][j]:
                    tmp += 1
            if tmp == 1 and not v[i]:
                v[i] = 1
                q.append((words[i], cnt+1))
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))