def solution(tickets):
    answer = []
    stack = ['ICN']
    v = [0]*len(tickets)

    def dfs(s, visited):
        if len(s) == len(tickets) + 1:
            # print(s)
            answer.append(list(s))
        start = stack[-1]
        for idx, ticket in enumerate(tickets):
            if ticket[0] == start and not v[idx]:
                v[idx] = 1
                stack.append(ticket[1])
                dfs(stack, v)
                v[idx] = 0
                stack.pop()

    dfs(stack, v)
    answer.sort()
    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))