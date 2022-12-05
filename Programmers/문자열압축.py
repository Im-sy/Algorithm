s = input()
l = len(s)
answer = l

# i 길이만큼 반복됨
for i in range(1, l // 2 + 1):
    # 같은 문자열 카운트
    tmp = 1
    # 압축 문자열 길이
    cnt = 0
    before = ""
    # 문자열 i 만큼 잘라서 비교
    for j in range(0, l, i):
        present = s[j:i + j]
        # 같다면, tmp 카운트
        if before == present:
            tmp += 1
        # 다르다면, cnt 카운트
        else:
            cnt += len(before)
            if tmp > 1:
                cnt += len(str(tmp))
            before = present
            tmp = 1
    # 남은 문자열 cnt 처리
    cnt += len(before)
    if tmp > 1:
        cnt += len(str(tmp))
    # 압축 문자열 최솟값 갱신
    answer = min(answer, cnt)

print(answer)