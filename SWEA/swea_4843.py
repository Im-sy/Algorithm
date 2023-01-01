T = int(input())
# 버블 정렬 함수
def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = bubblesort(arr) # 정렬한 후에
    result = []
    for i in range(5): # 특별한 정렬 적용
        result.append(arr[-i-1]) # 큰 수 부터
        result.append(arr[i]) # 작은 수 부터
    ans = ' '.join(map(str, result))
    print(f'#{tc} {ans}')