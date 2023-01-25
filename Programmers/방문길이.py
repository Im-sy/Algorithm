def solution(dirs):
    answer = 0
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    nr, nc = 0, 0
    for dir in dirs:
        dr, dc = d[dir]
        if -5>nr+dr or 5<nr+dr or -5>nc+dc or 5<nc+dc:
            continue
        go = (nr, nc, nr+dr, nc+dc)
        back = (nr+dr, nc+dc, nr, nc)
        if go not in visited:
            visited.add(go)
            visited.add(back)
            answer += 1
        nr, nc = nr + dr, nc + dc
    # print(visited)
    return answer


print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))
print(solution('UDUDUD'))