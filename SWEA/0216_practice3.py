def bruteforce(t, p):
    N = len(t)
    M = len(p)
    i = j = 0
    while i<N and j<M:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0
    if j == M:
        return True
    else:
        return False


print(bruteforce('this is a book', 'a b'))