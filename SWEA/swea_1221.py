import sys
sys.stdin = open('swea_1221.txt', 'r')

# 시간 : 314ms
# numbers = ["ZRO", "ONE", "TWO", "THR", "FOR",
#     "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())
# for _ in range(T):
#     tc, N = input().split()
#     arr = list(input().split())
#     print(tc)
#     for i in range(10):
#         for j in range(int(N)):
#             if numbers[i] == arr[j]:
#                 print(arr[j], end = ' ')
#     print()

# 시간 : 196ms
# numbers = ["ZRO", "ONE", "TWO", "THR", "FOR",
#     "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())
# for _ in range(T):
#     tc, N = input().split()
#     arr = list(input().split())
#     cnt = [0]*10
#     for i in range(10):
#         for j in range(int(N)):
#             if arr[j] == numbers[i]:
#                 cnt[i] += 1
#     result = []
#     for i in range(10):
#         for _ in range(cnt[i]):
#             result.append(numbers[i])
#     result = ' '.join(result)
#     print(f'{tc}\n{result}')

# 시간 초과
# numbers = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4,
#     "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
# T = int(input())
# for _ in range(T):
#     tc, N = input().split()
#     arr = list(input().split())
#     for i in range(int(N)-1, 0, -1):
#         for j in range(i):
#             if numbers[arr[j]] > numbers[arr[j+1]]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     print('{}\n{}'.format(tc, ' '.join(arr)))


# 교수님 풀이
GNS_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4,
    "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

def bubble_sort(target, N):
    for j in range(N-1):
        for i in range(N-1-j):
            if GNS_dict[target[i]] > GNS_dict[target[i+1]]:
                target[i], target[i+1] = target[i+1], target[i]

def select_sort(target, N):
    for i in range(N-1):
        # i번째 들어갈 요소 찾아서 i번에 넣어주기
        min_idx = 1
        # i번보다 인덱스가 빠른 것은 비교 X (이미 자리 찾음)
        for j in range(i+1, N):
            if GNS_dict[target[j]] < GNS_dict[target[min_idx]]:
                min_idx = j
        target[i], target[min_idx] = target[min_idx], target[i]

def counting_sort(target, N):
    count = [0]*10
    new_arr = [None]*N
    for i in range(N):
        count[GNS_dict[target[i]]] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(N):
        count[GNS_dict[target[i]]] -= 1
        new_arr[count[GNS_dict[target[i]]]] = target[i]
    return new_arr

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())
    # bubble_sort(arr, N)
    # print(arr)
    # select_sort(arr, N)
    # print(arr)
    print(tc, *counting_sort(arr, N))