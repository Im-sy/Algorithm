N = int(input())
cnt = N
for _ in range(N):
    S = input()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            continue
        elif S[i] in S[i+1:]:
            cnt -= 1
            break
print(cnt)