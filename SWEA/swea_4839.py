T = int(input())
def binarysearch(page, find):
    left = 1
    right = page
    mid = 0
    cnt = 1
    while find != mid:
        mid = (left + right) // 2
        if mid < find: # 찾는 값이 가운데 값보다 크면
            left = mid
        else: # 찾는 값이 가운데 보다 작으면
            right = mid
        cnt += 1
    return cnt

for tc in range(1, T+1):
    # 페이지 수, A가 찾을 페이지, B가 찾을 페이지
    P, Pa, Pb = map(int, input().split())
    A = binarysearch(P, Pa)
    B = binarysearch(P, Pb)
    if A < B:
        print(f'#{tc} A')
    elif A > B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')