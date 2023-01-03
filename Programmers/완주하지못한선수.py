# def solution(participant, completion):
#     while completion:
#         comp = completion.pop()
#         participant.remove(comp)
#     answer = participant.pop()
#     return answer


def solution(participant, completion):
    part = dict()
    for p in participant:
        try:
            part[p] += 1
        except:
            part[p] = 1
    for c in completion:
        if part[c] == 1:
            del part[c]
        else:
            part[c] -= 1
    answer = list(part.keys())
    return answer[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))