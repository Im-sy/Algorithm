from collections import deque
from collections import Counter
T = int(input())
for tc in range(1, T+1):
    F, N = map(int, input().split())
    arr = deque(map(int, input().split()))
    length = []
    tmp = 0
    for i in range(len(arr), -1, -1):
        tmp += i
        length.append(tmp)
    numbers = Counter(arr).most_common()
    Mnum = numbers[0][0]
    flag = 0
    for f in range(F):
        if f in length:
            numbers = Counter(arr).most_common()
            Mnum = numbers[0][0]
            flag = 0
        if len(arr)>1:
            first = arr.popleft()
            if first == Mnum and flag == 0:
                flag = 1
            else:
                arr.append(first)
        else:
            print(f'#{tc} {arr.popleft()}')
            break
    else: print(f'#{tc} {arr.pop()}')