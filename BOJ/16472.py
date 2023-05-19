N = int(input())
alpha = input()
# print(N, alpha)
l = len(alpha)
if N == 1 or l == 1:
    print(1)
elif len(set(alpha)) <= N:
    print(len(alpha))
else:
    i = 0
    j = i + 1
    answer = 1
    # while True:
        # if i == len(alpha)-2 :
        #     break
        # if j == len(alpha)+1 :
        #     i += 1
        #     j = i + 2
        # cut = alpha[i:j]
        # if len(set(cut)) <= N:
        #     j += 1
        #     answer = max(answer, len(cut))
        #     continue
        # else:
        #     j += 1

    while True:
        if i == l-1:
            break
        if l-i <= answer:
            break
        cut = [alpha[i]]
        cnt = 1
        while j <= l-1:
            pnt = alpha[j]
            cut.append(pnt)
            if len(set(cut)) <= N:
                # print(cut)
                cnt += 1
            else:
                break
            j += 1
        answer = max(answer, cnt)
        if j == l:
            break
        i += 1
        j = i + 1

    print(answer)