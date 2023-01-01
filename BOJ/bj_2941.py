S = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = cnt = 0
while i < len(S):
    if S[i:i+2] in alphabet:
        cnt += 1
        i += 2
    elif S[i:i+3] in alphabet:
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1
print(cnt)