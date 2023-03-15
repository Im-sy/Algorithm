def solution(n, computers):
    p = list(range(n))

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            p[b] = a
        else:
            p[a] = b

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(i, j)
    # print(p)
    answer = set()
    for i in range(n):
        answer.add(find(i))
    return len(answer)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))
print(solution(7, [
                [1,0,0,0,0,0,1],
                [0,1,1,0,1,0,0],
                [0,1,1,1,0,0,0],
                [0,0,1,1,0,0,0],
                [0,1,0,0,1,1,0],
                [0,0,0,0,1,1,1],
                [1,0,0,0,0,1,1]]))