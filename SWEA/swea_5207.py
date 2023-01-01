def binarysearch(l, r):
    if l>r:
        return
    m = (l+r) // 2
    if A[m] == target:
        result.append(0)
        return
    elif target < A[m]:
        result.append(1)
        binarysearch(l, m-1)
    else:
        result.append(2)
        binarysearch(m+1, r)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for target in B:
        result = []
        binarysearch(0, len(A)-1)
        if result[-1] == 0:
            if len(result) == 1:
                cnt += 1
            else:
                for i in range(0, len(result)-1):
                    if result[i] == result[i+1]:
                        break
                else:
                    cnt += 1
        # print(result, cnt)

    # 함수 없이 while 문으로 정답(시간 빠름)
    # ans = 0
    # for target in B:
    #     left = 0
    #     right = N-1
    #     flag = 0
    #     while left <= right:
    #         mid = (left+right)//2
    #         if target == A[mid]:
    #             ans += 1
    #             break
    #         elif target < A[mid]:
    #             right = mid - 1
    #             if flag == -1:
    #                 break
    #             flag = -1
    #         else:
    #             left = mid + 1
    #             if flag == 1:
    #                 break
    #             flag = 1

    print(f'#{tc} {cnt}')