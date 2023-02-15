def solution(s):
    answer = ''
    lst = s.split(' ')
    # print(lst)
    for e in lst:
        if e == '':
            answer += " "
            continue
        if e[0].isdigit():
            answer += e.lower() + " "
            continue
        answer += e.title() + " "
    return answer[:-1]


print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("  aa b  0c   "))