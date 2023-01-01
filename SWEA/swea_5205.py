# 퀵 정렬

# 시간 오래 걸림
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    left, mid, right = [], [], []
    for x in lst:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            mid.append(x)
    return quick_sort(left) + mid + quick_sort(right)

# lst 배열의 l, r 범위에서 피벗 정해서 큰값 작은값 분류
# 피벗 위치 반환
def partition(lst, l, r):
    pivot = lst[l]
    i = l
    j = r
    # i는 오른쪽으로 이동하면서 큰 값 찾기
    # j는 왼쪽으로 이동하면서 작은 값 찾기
    while i<=j:
        # 피벗보다 크면 i 증가 멈춤
        while i<=j and lst[i]<=pivot:
            i += 1
        # 피벗보다 작으면 j 감소 멈춤
        while i<=j and lst[j]>pivot:
            j -= 1
        if i>j:
            break
        else:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j

def quicksort(lst, l, r):
    # 더이상 자를 수 없음
    if l >= r:
        return
    # 피벗 선정
    s = partition(lst, l, r)
    # 피벗 기준 작은 값
    quicksort(lst, l, s-1)
    # 피벗 기준 큰 값
    quicksort(lst, s+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    # print(arr)
    # arr = quick_sort(arr)
    print(f'#{tc} {arr[N//2]}')