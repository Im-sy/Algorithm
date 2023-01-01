arr = [1, 2, 3, 4, 5]
N = 5
select = [0]*N
candidate = [0] * 2
def make_candidates():
    candidate[0] = 1
    candidate[1] = 0
    return 2

def ps(idx):
    if idx == N:
        for i in range(N):
            if select[i]:
                print(arr[i], end=' ')
        print()
        return
    num = make_candidates()
    for i in range(num):
        select[idx] = candidate[i]
        ps(idx+1)

ps(0)