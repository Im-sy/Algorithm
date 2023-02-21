def solution(n, words):
    v = [words[0]]
    who = 1
    num = 1
    tmp = words[0][-1]
    for i in range(1, len(words)):
        who += 1
        if who > n:
            who = 1
            num += 1
        if words[i].startswith(tmp) and words[i] not in v:
            tmp = words[i][-1]
            v.append(words[i])
            continue
        else:
            answer = [who, num]
            break
    else:
        answer = [0, 0]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))