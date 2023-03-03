def solution(s):
    stack = []
    if len(s)%2 != 0:
        return 0
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1
    ## 시간 초과
    # answer = 0
    # while True:
    #     if s == '':
    #         answer = 1
    #         break
    #     for i in range(len(s)-1):
    #         if s[i] == s[i+1]:
    #             s = s[:i] + s[i+2:]
    #             break
    #     else:
    #         break
    # return answer


print(solution('baabaa'))
print(solution('cdcd'))