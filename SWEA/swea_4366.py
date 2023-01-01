def solve(lst3):
    # 이진수 한자리씩 변경 -> 10진수 -> 3진수
    # num3과 한자리만 다르다면 ok
    for i in range(len(num2)):
        num2[i] = (num2[i] + 1) % 2
        dec = 0
        for idx in range(len(num2)):
            dec = dec * 2 + num2[idx]

        result = dec
        s = []
        while dec > 0:
            s.append(dec % 3)
            dec //= 3
        lst = lst3[::-1]

        # 다른 부분 카운트, 길이 다를 수 있음 주의
        cnt = 0
        for j in range(min(len(s), len(lst))):
            if s[j] != lst[j]:
                cnt += 1
        cnt += abs(len(s) - len(lst))

        if cnt == 1:
            return result

        # 원래대로
        num2[i] = (num2[i] + 1) % 2


T = int(input())
for tc in range(1, T + 1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))
    ans = solve(num3)
    print(f'#{tc} {ans}')