from collections import Counter

def solution(s):
    s = s.lower()
    cnt = Counter(s)
    if cnt['p'] == cnt['y']:
        return True
    else:
        return False



print(solution("pPoooyY"))
print(solution("Pyy"))