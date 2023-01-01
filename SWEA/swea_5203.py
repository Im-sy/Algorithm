def check(lst):
    for i in range(10):
        if lst[i] >= 3:
            return True
        if lst[i] and lst[i+1] and lst[i+2]:
            return True
    return False


def babygin(lst):
    cnt = [0]*12
    for i in range(6):
        cnt[lst[i]] += 1
        if i >= 2 and check(cnt):
            return i
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1, p2 = [], []
    for i in range(0, 11, 2):
        p1.append(arr[i])
        p2.append(arr[i+1])
    # print(p1, p2)
    # print(babygin(p1), babygin(p2))
    a, b = babygin(p1), babygin(p2)
    if a==0 or b==0:
        if a > b:
            ans = 1
        elif a < b:
            ans = 2
        else:
            ans = 0
    else:
        if a > b:
            ans = 2
        else:
            ans = 1
    print(f'#{tc} {ans}')