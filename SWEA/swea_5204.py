def merge(l, r):
    global cnt
    result = []
    # while len(l)>0 or len(r)>0:
    #     if len(l)>0 and len(r)>0:
    #         if l[0] <= r[0]:
    #             result.append(l.pop(0))
    #         else:
    #             result.append(r.pop(0))
    #     elif len(l)>0:
    #         if len(l) == 1:
    #             cnt += 1
    #         result.append(l.pop(0))
    #     elif len(r)>0:
    #         result.append(r.pop(0))
    # print(result, cnt)

    i, j = 0, 0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    while i<len(l):
        if i+1 == len(l):
            cnt += 1
        result.append(l[i])
        i += 1
    while j<len(r):
        result.append(r[j])
        j += 1
    # print(result, cnt)
    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    left = mergesort(lst[:len(lst)//2])
    right = mergesort(lst[len(lst)//2:])
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sort_arr = mergesort(arr)
    print(f'#{tc} {sort_arr[N//2]} {cnt}')