A, B = input().split()
for i in range(2, -1, -1):
    if A[i] > B[i]:
        for a in range(2, -1, -1):
            print(A[a], end='')
        break
    elif A[i] < B[i]:
        for b in range(2, -1, -1):
            print(B[b], end='')
        break
