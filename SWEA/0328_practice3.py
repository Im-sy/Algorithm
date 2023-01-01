n = int(input())
arr = list(map(int, input().split()))

def powerset(idx, selected):
    global cnt
    if idx == n:
        tmp = 0
        for i in range(n):
            if selected[i]:
                tmp += arr[i]
        if tmp == 0:
            cnt += 1
        return
    selected[idx] = 0
    powerset(idx + 1, selected)
    selected[idx] = 1
    powerset(idx+1, selected)

cnt = 0
powerset(0, [0]*n)
