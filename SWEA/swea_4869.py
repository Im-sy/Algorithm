T = int(input())

for tc in range(1, T+1):
    N = int(input())
    paper = [0]*(N//10)
    paper[0] = 1
    paper[1] = 3
    for i in range(2, N//10):
        paper[i] = paper[i-1] + 2*paper[i-2]
    print(f'#{tc} {paper[-1]}')