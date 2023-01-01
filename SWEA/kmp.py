def kmp(t, p):
    N = len(t) # 패턴이 있는지 찾고자 하는 대상 문자열 길이
    M = len(p) # 패턴의 길이
    # lps : longest proper prefix which is also suffix
    lps = [0]*(M+1)
    lps[0] = -1
    # 사전작업 : 매칭이 실패했을 때 패턴의 어느 인덱스로 돌아가야하는지 계산
    j = 0 # 일치한 개수 저장하는 변수
    for i in range(1, M):
        # 앞쪽에 얼마나 많은 패턴이 맞았는지
        lps[i] = j
        # 앞서서 패턴이 일치했으면 j 증가
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # 패턴 매칭 시작
    i = 0 # 비교 텍스트 위치
    j = 0 # 패턴 시작위치
    while i < N:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            # shift 찾기
            j = lps[j]
        if j == M: # 패턴 찾음
            # print('있다!')
            return True
            # j = lps[j]
    return False

print(kmp('abcdeabcfg', 'abc'))