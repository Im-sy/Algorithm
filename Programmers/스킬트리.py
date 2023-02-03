def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = ''
        for t in tree:
            if t in skill:
                tmp += t
        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                break
        else:
            answer += 1
            print(tree, tmp)
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))