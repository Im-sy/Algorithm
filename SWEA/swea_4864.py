T = int(input())
# 고지식한 패턴 검색 브루트포스
def bruteforce(target, pattern):
    N = len(target)
    M = len(pattern)
    i = j = 0
    while i<N and j<M:
        if target[i] == pattern[j]:
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0
    if j == M:
        return 1
    else:
        return 0

# KMP
def kmp(target, pattern):
    N = len(target)
    M = len(pattern)
    # 불일치 발생 시 이동할 다음 위치 저장
    lps = [0]*(M+1)
    lps[0] = -1
    j = 0 # 일치한 개수 저장할 변수
    for i in range(1, M):
        lps[i] = j # 앞에서 몇개나 일치했는지 저장
        if pattern[i] == pattern[j]: # 앞에서 패턴 일치 시
            j += 1
        else: # 일치하는 것 없을 시
            j = 0
    lps[M] = j

    i = j = 0
    while i<N:
        if j == -1 or target[i] == pattern[j]:
            i += 1
            j += 1
        else: # 불일치 발생, 이동할 위치
            j = lps[j]
        if j == M: # pattern 찾을 시
            return 1
    return 0

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result1 = bruteforce(str2, str1)
    result2 = kmp(str2, str1)
    print(f'#{tc} {result1}')
    print(f'#{tc} {result2}')