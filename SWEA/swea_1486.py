T = int(input())

def powerset(idx, selected):
    if idx==N:
        tmp_sum = 0
        for i in range(N):
            if selected[i]:
                tmp_sum += arr[i]
        if tmp_sum >= B:
            height.append(tmp_sum-B)
        return
    selected[idx] = 0
    powerset(idx+1, selected)
    selected[idx] = 1
    powerset(idx+1, selected)

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    selected = [0]*N
    height = []
    powerset(0, selected)
    print(f'#{tc} {min(height)}')