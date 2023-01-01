T = int(input())
def bruteforce(target, pattern):
    N = len(target)
    M = len(pattern)
    i = j = cnt = 0
    while i<N:
        if target[i] == pattern[j]:
            if j == M - 1:
                i += 1
                j = 0
                cnt += 1
                continue
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0

    return cnt

for tc in range(1, T+1):
    A, B = input().split()
    result = len(A) - bruteforce(A, B)*(len(B)-1)
    print(f'#{tc} {result}')