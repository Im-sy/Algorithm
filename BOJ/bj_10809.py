S = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    for idx in range(len(S)):
        if i == S[idx]:
            print(idx, end = ' ')
            break
    else:
        print(-1, end = ' ')
