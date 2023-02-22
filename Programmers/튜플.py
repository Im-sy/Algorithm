def solution(s):
    s = s[2:-2].split('},{')
    s = [set(item.split(',')) for item in s]
    s.sort(key=lambda x:len(x))
    # print(s)
    answer = [int((s[0] - set()).pop())]
    for i in range(1, len(s)):
        answer.append(int((s[i] - s[i-1]).pop()))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))