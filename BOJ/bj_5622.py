S = input()
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for s in S:
    for i in range(len(alphabet)):
        for x in alphabet[i]:
            if s == x:
                cnt += i+3
print(cnt)
